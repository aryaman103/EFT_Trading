# backend/data_pipeline.py
import os
import yfinance as yf
import feedparser
import pandas as pd
from langchain.embeddings import HuggingFaceEmbeddings
import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    persist_directory="./chroma_db",     # or another path
    chroma_db_impl="duckdb+parquet"      # required since 0.4+
))

from dotenv import load_dotenv

load_dotenv()

ETFS = os.getenv("ETFS", "SPY,QQQ").split(",")
RSS_URLS = os.getenv("RSS_URLS", "https://finance.yahoo.com/rss/topstories").split(",")
CHROMA_PATH = os.getenv("CHROMA_PATH", "../data/chroma/")

# 1. Download OHLCV
def download_ohlcv():
    data = {}
    for etf in ETFS:
        df = yf.download(etf, period="30d", interval="1d")
        data[etf] = df
        df.to_csv(f"../backend/data/{etf}_ohlcv.csv")
    return data

# 2. Parse RSS titles
def fetch_rss_titles():
    titles = []
    for url in RSS_URLS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            titles.append(entry.title)
    return titles

# 3. Embed with MiniLM and store in Chroma
def embed_and_store(titles):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    client = Client(Settings(persist_directory=CHROMA_PATH, chroma_db_impl="sqlite"))
    collection = client.get_or_create_collection("news_titles")
    vectors = embeddings.embed_documents(titles)
    for i, (title, vec) in enumerate(zip(titles, vectors)):
        collection.add(
            documents=[title],
            embeddings=[vec],
            ids=[str(i)]
        )
    client.persist()

if __name__ == "__main__":
    download_ohlcv()
    titles = fetch_rss_titles()
    embed_and_store(titles) 
# FinSight

**FinSight** is an end-to-end demo project that integrates reinforcement learning (RL) and retrieval-augmented generation (RAG) to simulate intelligent ETF trading. Built to showcase how modern AI techniques can be combined for real-world financial applications, the project uses RLlib's PPO algorithm to train a custom Gymnasium environment to trade between two ETFs based on both price-based indicators and sentiment analysis. A lightweight RAG pipeline processes real-time RSS news, generates embeddings with MiniLM, stores them in ChromaDB, and summarizes with GPT before feeding sentiment into the agent's state. The backend is powered by FastAPI for predictions and live streaming, while the frontend offers a sleek Vite + React dashboard with real-time charts. FinSight exists as a compact but powerful demonstration of how multiple AI tools—RL, LLMs, vector stores, and web apps—can come together in a unified, Dockerized environment for rapid experimentation and learning.


---

## Project Structure

```
finsight-alpha-lite/
├── backend/      # FastAPI, RLlib PPO, data pipeline, sentiment, env
├── frontend/     # Vite + React + Tailwind + Recharts dashboard
├── notebooks/    # Jupyter backtest notebook
├── infra/        # Docker Compose, devcontainer, scripts
├── tests/        # Pytest unit tests
├── docs/         # Documentation (this file)
```

---

## Key Components

- **RLlib PPO**: Custom Gymnasium env for two ETFs, state = [price_pct_change, rolling_vol, sentiment_score].
- **RAG Pipeline**: RSS → MiniLM embeddings → ChromaDB → GPT summary stub → DistilBERT sentiment.
- **FastAPI**: `/predict` endpoint (action/weight), websocket for live equity curve.
- **React Dashboard**: Tabs for dashboard, sentiment feed, trades; live charts via websocket.

---

## Dev Environment
- Python 3.11 (Poetry)
- Node 18 (Vite, React, Tailwind)
- Docker Compose (all-in-one stack)
- VSCode devcontainer support

---

## Testing
- Run all tests:
  ```sh
  poetry run pytest ../tests
  ```

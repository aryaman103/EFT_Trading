# docs/README.md

# FinSight Alpha-Lite

**End-to-end RL + RAG ETF trading demo**

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

## Quickstart

1. **Clone repo & set up .env**
   - Copy `.env.example` to `.env` and fill in your `OPENAI_API_KEY` (or leave as stub for offline mode).

2. **Build & run all services**
   ```sh
   cd infra
   bash start.sh
   ```
   - This launches:
     - `api` (FastAPI backend, RLlib PPO)
     - `frontend` (React dashboard)
     - `chromadb` (SQLite vector DB)

3. **Access the dashboard**
   - Open [http://localhost:5173](http://localhost:5173)

4. **Run the data pipeline**
   ```sh
   cd ../backend
   poetry run python data_pipeline.py
   ```

5. **Train the PPO agent**
   ```sh
   poetry run python trainer.py
   ```

6. **Backtest in notebook**
   - Open `notebooks/backtest.ipynb` in Jupyter.

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

---

## Notes
- For offline mode, GPT summary is stubbed.
- ChromaDB runs in SQLite mode for easy local dev.
- Extendable to more ETFs, news sources, or LLMs.

---

## Authors
- Quant/ML/Infra: [Your Name] 
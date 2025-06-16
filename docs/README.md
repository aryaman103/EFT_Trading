# FinSight

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

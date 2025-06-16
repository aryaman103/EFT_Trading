# backend/main.py
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import numpy as np
import os
import asyncio

app = FastAPI()

# Dummy model for demonstration
class PredictRequest(BaseModel):
    etfs: list[str] = ["SPY", "QQQ"]

@app.post("/predict")
async def predict(req: PredictRequest):
    # In production, load PPO policy and compute action/weight
    action = np.random.choice([0, 1, 2])  # 0: cash, 1: ETF1, 2: ETF2
    weight = float(np.random.uniform(0, 1))
    return {"action": int(action), "weight": weight}

@app.websocket("/ws/metrics")
async def metrics_ws(websocket: WebSocket):
    await websocket.accept()
    # Dummy equity curve stream
    equity = 100.0
    while True:
        equity += np.random.normal(0, 0.5)
        await websocket.send_json({"equity": equity})
        await asyncio.sleep(1) 
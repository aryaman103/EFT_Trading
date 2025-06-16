# backend/trainer.py
import os
import torch
import pandas as pd
from ray.rllib.algorithms.ppo import PPOConfig
from ray.rllib.algorithms.algorithm import Algorithm
from ray.tune.registry import register_env
from dotenv import load_dotenv
from env import ETFEnv

load_dotenv()

ETFS = os.getenv("ETFS", "SPY,QQQ").split(",")
DATA_PATH = "../backend/data/"
MODEL_PATH = "../backend/models/policy.pkl"


def load_data():
    dfs = [pd.read_csv(f"{DATA_PATH}{etf}_ohlcv.csv") for etf in ETFS]
    return dfs

def make_env(config):
    dfs = load_data()
    return ETFEnv(dfs=dfs)

register_env("ETFEnv", make_env)

if __name__ == "__main__":
    config = PPOConfig().environment(env="ETFEnv", env_config={})
    algo = config.build()
    for _ in range(10):
        results = algo.train()
        print(f"Iter: {_}, reward: {results['episode_reward_mean']}")
    algo.save(MODEL_PATH) 
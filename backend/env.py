# backend/env.py
import gymnasium as gym
import numpy as np

class ETFEnv(gym.Env):
    def __init__(self, dfs=None):
        super().__init__()
        self.dfs = dfs
        self.n_etfs = 2
        self.current_step = 0
        self.window = 5
        self.action_space = gym.spaces.Discrete(self.n_etfs + 1)  # cash, ETF1, ETF2
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(3,), dtype=np.float32)
        self.sentiment = 0.0
        self.reset()

    def reset(self, seed=None, options=None):
        self.current_step = self.window
        self.equity = 1.0
        obs = self._get_obs()
        return obs, {}

    def step(self, action):
        done = self.current_step >= len(self.dfs[0]) - 1
        reward = 0.0
        if not done:
            pct_change = self.dfs[action-1]["Close"].pct_change().iloc[self.current_step] if action > 0 else 0.0
            reward = pct_change
            self.equity *= (1 + reward)
        self.current_step += 1
        obs = self._get_obs()
        return obs, reward, done, False, {}

    def _get_obs(self):
        idx = self.current_step
        price_pct = [df["Close"].pct_change().iloc[idx] for df in self.dfs]
        rolling_vol = [df["Close"].pct_change().rolling(self.window).std().iloc[idx] for df in self.dfs]
        # For demo, sentiment is random
        sentiment_score = self.sentiment if hasattr(self, 'sentiment') else np.random.uniform(-1, 1)
        return np.array([
            np.mean(price_pct),
            np.mean(rolling_vol),
            sentiment_score
        ], dtype=np.float32) 
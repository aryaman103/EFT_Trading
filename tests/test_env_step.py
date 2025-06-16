# tests/test_env_step.py
import pytest
import numpy as np
from backend.env import ETFEnv

class DummyDF:
    def __init__(self, n):
        self.data = np.ones(n)
    def __getitem__(self, key):
        class Dummy:
            def pct_change(self):
                return np.zeros(30)
            def rolling(self, w):
                class Roll:
                    def std(self):
                        return np.ones(30)
                return Roll()
        return Dummy()
    def __len__(self):
        return 30

def test_env_reset_and_step():
    dfs = [DummyDF(30), DummyDF(30)]
    env = ETFEnv(dfs=dfs)
    obs, _ = env.reset()
    assert obs.shape == (3,)
    obs2, reward, done, _, _ = env.step(1)
    assert obs2.shape == (3,)
    assert isinstance(reward, float)
    assert isinstance(done, bool) 
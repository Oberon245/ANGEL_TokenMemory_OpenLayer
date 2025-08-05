
import math
from collections import defaultdict
import pandas as pd

class TokenMemory:
    def __init__(self, decay_rate=0.01):
        self.token_data = defaultdict(lambda: {"weight": 0.0, "count": 0, "last_seen": 0, "intensity": 1.0})
        self.step = 0
        self.decay_rate = decay_rate

    def update(self, tokens, intensity=1.0):
        self.step += 1
        for token in tokens:
            data = self.token_data[token]
            time_diff = self.step - data["last_seen"]
            decay = math.exp(-self.decay_rate * time_diff)
            data["weight"] = data["weight"] * decay + intensity
            data["count"] += 1
            data["last_seen"] = self.step
            data["intensity"] = intensity

    def to_dataframe(self):
        return pd.DataFrame([
            {"token": token, **vals}
            for token, vals in self.token_data.items()
        ]).sort_values(by="weight", ascending=False)

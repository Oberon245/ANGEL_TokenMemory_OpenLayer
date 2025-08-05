"""
Relational Token Memory Layer
Tracks token weights for two participants and calculates relational salience drift.
"""
import json
from collections import defaultdict
import math

class TokenMemory:
    def __init__(self, name, decay=0.95):
        self.name = name
        self.token_weights = defaultdict(float)
        self.decay = decay

    def update_weights(self, tokens, intensity=1.0):
        for token in tokens:
            self.token_weights[token] += intensity

    def decay_weights(self):
        for token in self.token_weights:
            self.token_weights[token] *= self.decay

    def get_weights(self):
        return dict(self.token_weights)

class RelationalMemorySystem:
    def __init__(self, decay=0.95):
        self.systems = {
            "User": TokenMemory("User", decay),
            "AI": TokenMemory("AI", decay)
        }

    def step(self, user_tokens, ai_tokens, user_intensity=1.0, ai_intensity=1.0):
        self.systems["User"].update_weights(user_tokens, user_intensity)
        self.systems["AI"].update_weights(ai_tokens, ai_intensity)
        self.systems["User"].decay_weights()
        self.systems["AI"].decay_weights()

    def compute_drift(self):
        drift = {}
        user_weights = self.systems["User"].get_weights()
        ai_weights = self.systems["AI"].get_weights()
        all_tokens = set(user_weights.keys()) | set(ai_weights.keys())
        for token in all_tokens:
            drift[token] = user_weights.get(token, 0) - ai_weights.get(token, 0)
        return drift

    def export_memory(self, filepath="memory_export.json"):
        data = {
            name: sys.get_weights() for name, sys in self.systems.items()
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

    def export_drift(self, filepath="drift_log.csv"):
        drift = self.compute_drift()
        with open(filepath, "w") as f:
            f.write("Token,Drift
")
            for token, value in drift.items():
                f.write(f"{token},{value:.3f}\n")

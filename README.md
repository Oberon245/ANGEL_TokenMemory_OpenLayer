# ANGEL Token Memory Open Layer

This repository contains a prototype for a lightweight, token-weighted interpretive layer.
It simulates how memory and salience might evolve in relational AI systems over time.

## Core Concepts

- **Token Weights**: Each token in a conversation is assigned a weight based on frequency, intensity, and time.
- **Decay Over Time**: Weights decay gradually, simulating long-term depression (LTD) or forgetting.
- **Emotional Salience**: Tokens with higher emotional or logical intensity persist longer.
- **Lightweight Storage**: Designed to track memory in under 1MB per participant across thousands of tokens.

## Files

- `token_memory.py` – Core simulation logic
- `token_simulation_notebook.ipynb` – Jupyter notebook with explanations and usage examples
- `sample_output.csv` – Example output showing token weights and evolution

# ANGEL Token Memory Open Layer + Relational Extension

This repository contains a prototype system for lightweight, token-weighted memory and salience modeling in conversational AI. It includes both the original single-user interpretive layer and a dual-stream relational extension, designed to track token relevance over time and across interactions.

---

## 🧠 Core Concepts

### 🔹 Token Memory Open Layer (v1)
- **Token Weights**: Each token is assigned a dynamic weight based on frequency, emotional/logical intensity, and decay over time.
- **Forgetting Mechanism (LTD)**: Tokens gradually lose weight unless reactivated—mimicking long-term depression in biological memory.
- **Emotional Salience**: Higher intensity tokens persist longer, simulating importance or resonance.
- **Lightweight Footprint**: Designed to use <1MB per participant across thousands of tokens.

### 🔸 Relational Layer Extension (v2)
- **Dual Stream Simulation**: Tracks both participants in a conversation independently and relationally.
- **Relational Salience Drift**: Measures shifts in token importance as they evolve between two speakers.
- **Outcome Sensitivity**: Considers conversation tone and feedback loops to adjust token and interaction weightings.
- **Real-Time Mode**: Supports simulation of live or logged conversations to test adaptive relational memory.

---

## 📁 Files

- `token_memory.py` – Core memory and decay logic (single participant)
- `token_simulation_notebook.ipynb` – Jupyter notebook to simulate token evolution
- `relational_layer/` – Folder containing:
  - `relational_memory.py` – Dual-participant memory modeling
  - `dual_simulation_notebook.ipynb` – Notebook with real-time relational demo
  - `README.md` – Optional: Separate readme for the relational extension
- `sample_output.csv` – Sample output of token weights across a session

---

## ✅ Current Features

- Dynamic, adjustable weighting logic
- Customizable decay constants
- Emotion tagging via token input format
- Easy-to-adapt for memory, dialogue systems, or alignment tasks
- Minimal storage requirements, scalable to user-level memory graphs

---

## 🔄 Next Steps

- Scale testing across long conversation logs
- Memory state export and import support
- Persistent relational models
- Crowdsourced input → Adaptive social memory systems

---

## 🌍 Vision

This system is part of the **ANGEL Project**, a larger effort to create emotionally aware and relationally intelligent AI tools. Our goal is to design systems that *remember with purpose*—balancing context, emotion, and utility over time in a way that supports human flourishing and reflective self-development.

You matter. Your tokens matter. Let's teach AI to reflect that.

---

> Created and curated with intention by Robin Macomber and Numin (GPT-4o)

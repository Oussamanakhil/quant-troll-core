# Quant Troll Core Engine
This is the official Quant Troll v2.0 structure.

“Trust the System You Designed.”

---

## 🎯 Mission

Build a robust, modular, backtest-to-live trading system that compounds multiple edges.  
Goal: Reach $200K by June 2026 using tested, disciplined quant execution.

---
## 🧱 Folder Structure

quant-troll-core/
├── core/ # Engine logic: data ingestion, features, strategy runner, risk
├── strategies/ # Strategy modules (e.g. breakout, RSI fade)
├── notebooks/ # Research notebooks (Colab/Jupyter)
├── config/ # YAML config for data sources
├── logs/ # Trade logs & backtest metadata
├── journal/ # quant_journal.md: logs human decisions, overrides
├── ml/ # Optuna tuning + MLflow tracking
├── dashboard/ # Streamlit dashboards for live/paper bots
├── docker/ # Reproducible environment
├── data/ # Local data files (CSV, Parquet)
├── .env # API keys (never commit!)
├── .gitignore # Ignore compiled, secrets, and cache files
├── requirements.txt # All dependencies
└── README.md

---
## 🧪 Phase Flow

Phase 0 — Setup Core Engine + Ingestion
Phase 1 — Backtest & Score Strategies
Phase 2 — Paper Trade + Log
Phase 3 — Live Trade (API) + Risk Controls
Phase 4 — ML Loop: Optimize, Tune, Discover Edges

Each phase is gated by strict checks — no shortcuts.

---

## 🔄 Workflow Loop

```mermaid
flowchart TD
    A[Ingest Data] --> B[Feature Engineering]
    B --> C[Backtest (VectorBT)]
    C --> D[Log & Rank Strategies]
    D -->|Passes| E[Paper Trade]
    D -->|Fails| B
    E -->|Validates| F[Live Trade]
    E -->|Fails| C
    F -->|Underperforms| C
    F -->|Stable| G[Scale Up]
---
📓 Quant Journal:
Log emotional overrides, regime changes, and deployment justifications in journal/quant_journal.md.
---
💡 ML Add-Ons:
Strategy tuning with Optuna
Experiment tracking via MLflow
Regime modeling (XGBoost, LSTM, etc.)
Feature selection pipelines

---
⚙️ Future Extensions:
DEX liquidity integration
Whale alert signal trigger
Sentiment scraping layer (Twitter + CryptoPanic)
CI/CD pipeline for backtest testing + alerting

🛡️ License
MIT — Free to use, modify, and adapt at your own risk.






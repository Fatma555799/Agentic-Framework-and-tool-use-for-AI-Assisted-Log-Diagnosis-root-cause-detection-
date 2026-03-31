# 🚁 ArduPilot Agentic Log Diagnosis Framework

**AI-Powered Agent for Automated Flight Log Analysis and Root Cause Detection**

An intelligent, tool-using AI agent that helps ArduPilot users and developers diagnose crashes, anomalies, and misconfigurations in `.BIN` flight logs quickly and reliably.

---

## ✨ Project Overview

Analyzing ArduPilot flight logs after a crash or anomaly is traditionally a manual, time-consuming process that requires deep domain expertise.

This project builds an **Agentic Framework** — an LLM-powered agent that uses a set of specialized tools to:
- Parse `.BIN` (DataFlash) logs
- Extract meaningful features
- Apply physics-informed rules
- Perform step-by-step reasoning
- Output probable root causes, suggested fixes, calibrated confidence scores, and direct evidence links from the log

The framework is designed to be **interpretable**, **grounded**, and **safe** (with abstention mechanism when confidence is low).

This work is complementary to the **AI Log Analyzer** developed in GSoC 2025.

---

## 🎯 Key Features (Current - Demo Phase)

- Robust `.BIN` log parsing using `pymavlink`
- Safe and dynamic feature extraction (Vibration, Battery, Error messages, etc.)
- Physics-informed rule engine with clear evidence linking
- Simple ReAct-style agent for step-by-step diagnosis
- CLI tool for easy usage: `python demo_agent.py your_log.bin`
- High interpretability: every diagnosis comes with evidence and confidence score

---

## 🛠️ Installation

### Prerequisites
- Python 3.10+
- ArduPilot development environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Fatma555799/Agentic-Framework-and-tool-use-for-AI-Assisted-Log-Diagnosis-root-cause-detection.git
   cd Agentic-Framework-and-tool-use-for-AI-Assisted-Log-Diagnosis-root-cause-detection
2.Install dependencies:
Bash
pip install -r requirements.txt

Quick Start / Usage
Basic Demo (Rule-based)
Bashpython demo_agent.py path/to/your_flight_log.bin
Example Output:

Detected Issues with severity and confidence
Clear evidence (timestamps + message values)
Suggested fixes with links to ArduPilot Wiki
Overall confidence score


📁 Project Structure
textagentic-log-diagnoser/
├── demo_agent.py                    # Simple rule-based demo
├── log_parser.py              # .BIN parser + feature extraction
├── rule_engine.py             # Physics-informed rules
├── agent.py                   # Basic agent logic
├── tools.py                   # Tool definitions
├── inspect_log.py             # Helper to inspect log content
├── requirements.txt
└── README.md

🧠 Technical Approach

Hybrid Architecture: Rule-based engine + LLM agent + (future) ML classifier
Tool-Use: The agent can call multiple tools in sequence (parser, rules, retrieval, etc.)
Grounding: All outputs are backed by real evidence from the log to minimize hallucinations
Confidence Calibration & Abstention: The system says "Inconclusive" when confidence is low


🔮 Future Enhancements (Roadmap)
Phase 1 (Foundation - Done in Demo)

Robust parser and basic feature extraction
Rule engine with 10+ common failure modes

Phase 2 (Tools & ML)

Full feature pipeline (25–40 domain-specific features)
Machine Learning classifier (XGBoost or similar) as an additional tool
Case-based retrieval (similar historical logs)
Hybrid orchestration layer

Phase 3 (Full Agentic Framework)

Advanced ReAct / tool-calling agent (LLM-agnostic)
Confidence calibration system
CLI tool + basic web interface (Streamlit)
Integration with existing AI Log Analyzer (GSoC 2025)
Comprehensive documentation and evaluation on real + SITL logs

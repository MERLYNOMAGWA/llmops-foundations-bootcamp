# 🧠 LLMOps Chatbot Project

## 📌 Overview

This project demonstrates a **mini LLMOps lifecycle** for a chatbot system. It covers:

- System design (with lifecycle map diagram)
- Monitoring and logging
- Feedback collection
- Rollback strategy for stability
- Security & compliance considerations

---

## 🚀 Onboarding / Setup

1. **Clone the repo**:

   ```bash
   git clone https://github.com/your-username/llmops-chatbot.git
   cd llmops-chatbot

   ```

2. **Set up virtual environment**

python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

3. **Install dependencies:**

pip install -r requirements.txt

4. **🗺️ System Diagram**
   LLMOps Lifecycle (Mermaid.js)
   mermaid

flowchart LR
A[Deploy] --> B[Monitor]
B --> C[Evaluate]
C --> D[Version Control]
D --> E[Feedback Collection]
E --> F[Improve & Retrain]
F --> A
**Explanation of phases:**

Deploy → Initial chatbot release for users.

Monitor → Track latency, errors, and privacy risks.

Evaluate → Measure response quality and compliance.

Version Control → Manage main and stable branches (rollback ready).

Feedback Collection → Gather user/PM input (manual or JSON).

Improve & Retrain → Apply feedback to refine chatbot model.

## 💻 Code Usage

1. **Run Monitoring**
   Simulate chatbot logs, detect PII, and log latency/errors:

python monitoring.py
Outputs to: monitoring.log (human-readable) and monitoring.json (structured logs).

2. **Run Feedback Collector**
   Option 1: Interactive mode

python feedback_collector.py
Option 2: Load from JSON (coming soon)

## 🔄 Rollback Strategy

We maintain two branches:

main → active development, newest features.

stable → last known good state.

**Rollback scenario:**
If a deployment on main fails (e.g., errors, compliance issues), revert:

git checkout stable
git merge -s ours main # keep stable’s state
git push origin stable
This ensures production always runs on stable until fixes are applied.

## 🔒 Security & Compliance Notes

PII Detection: Regex checks for emails/phone numbers in responses.

Error Handling: Logs all failures and empty responses.

Latency Monitoring: Flags slow responses.

Compliance: System avoids exposing sensitive financial details.

## ✨ Design Choices

Used Mermaid.js for lifecycle diagram (lightweight, Markdown-native).

Logs are stored in both plain text and JSON for human + machine use.

Feedback is collected interactively first, then extended to batch JSON.

Git branching (main + stable) ensures safe rollback paths.

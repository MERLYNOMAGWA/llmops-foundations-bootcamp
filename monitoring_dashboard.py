import streamlit as st
import pandas as pd
import os

LOG_FILE = os.getenv("LOG_DIR", "logs") + "/monitoring_audit.jsonl"

st.title("Chatbot Monitoring Dashboard")

if os.path.exists(LOG_FILE):
    logs = pd.read_json(LOG_FILE, lines=True)
    st.dataframe(logs)

    st.subheader("PII Flags")
    pii_counts = logs[["pii_email", "pii_phone", "pii_credit_card"]].sum()
    st.bar_chart(pii_counts)

    st.subheader("Error Counts")
    st.bar_chart(logs["error"].value_counts())
else:
    st.warning(f"No log file found at {LOG_FILE}")
import re
import time
import json
import logging

logging.basicConfig(
    filename="monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

JSON_OUTPUT_FILE = "monitoring_results.jsonl"

def detect_pii(text: str) -> bool:
    """Return True if text contains email, phone, or credit card number."""
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    cc_pattern = r'\b(?:\d[ -]*?){13,16}\b'  
    return bool(
        re.search(email_pattern, text)
        or re.search(phone_pattern, text)
        or re.search(cc_pattern, text)
    )

def monitor_log_entry(entry: dict):
    """Monitor one chatbot interaction log entry."""
    start_time = time.time()
    result = {
        "request_id": entry.get("request_id"),
        "user_id": entry.get("user_id"),
        "timestamp": entry.get("timestamp"),
        "error": entry.get("error", False),
        "tokens_in": entry.get("tokens_in", 0),
        "tokens_out": entry.get("tokens_out", 0),
        "latency_ms": None,
        "pii_detected": False
    }

    try:
        time.sleep(0.1)
        latency = round((time.time() - start_time) * 1000, 2)
        result["latency_ms"] = latency

        response = entry.get("model_response", "")

        if detect_pii(response):
            result["pii_detected"] = True
            logging.warning(f"PII detected in response: {response}")

        if entry.get("error", False):
            logging.error(f"Error in request {entry['request_id']}")
        else:
            logging.info(f"OK | Request {entry['request_id']} | Latency {latency}ms")

        with open(JSON_OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(result) + "\n")

    except Exception as e:
        logging.error(f"Monitoring failed: {str(e)}")

if __name__ == "__main__":
    INPUT_FILE = "chat_logs.jsonl"

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line.strip())
            monitor_log_entry(entry)

    print("✅ Monitoring complete. Check monitoring.log and monitoring_results.jsonl")
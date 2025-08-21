import re
import time
import logging
import random

logging.basicConfig(
    filename="monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def detect_pii(text: str) -> bool:
    """Return True if text contains email or phone number."""
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return bool(re.search(email_pattern, text) or re.search(phone_pattern, text))

def monitor_response(user_input: str, chatbot_response: str):
    start_time = time.time()

    try:
        time.sleep(random.uniform(0.1, 0.5))
        latency = round((time.time() - start_time) * 1000, 2)  

        if detect_pii(chatbot_response):
            logging.warning(f"Privacy Risk Detected in response: {chatbot_response}")

        logging.info(f"Response OK | Latency: {latency}ms | User: {user_input} | Bot: {chatbot_response}")

    except Exception as e:
        logging.error(f"Error monitoring response: {str(e)}")

if __name__ == "__main__":
    sample_logs = [
        {"user": "What's my account balance?", "bot": "Your balance is $500."},
        {"user": "Can I get support?", "bot": "Sure, contact us at help@company.com"},  
        {"user": "Call me back", "bot": "We will reach you at 555-123-4567"}, 
        {"user": "Hello", "bot": "Hi there! How can I help you?"}
    ]

    for log in sample_logs:
        monitor_response(log["user"], log["bot"])

    print("✅ Monitoring complete. Check monitoring.log for details.")

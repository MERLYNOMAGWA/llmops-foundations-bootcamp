import json
import datetime
import os

FEEDBACK_FILE = "feedback.jsonl"

def validate_feedback(feedback: dict) -> bool:
    """Check if feedback contains required fields."""
    required_fields = ["timestamp", "user_id", "feedback_type", "description"]
    return all(field in feedback and feedback[field] for field in required_fields)

def save_feedback(feedback: dict):
    """Append feedback to a JSONL file if valid."""
    if validate_feedback(feedback):
        with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(feedback) + "\n")
        print("✅ Feedback saved.")
    else:
        print("❌ Invalid feedback. Missing required fields.")

def collect_feedback():
    """Interactive CLI to collect feedback from a user."""
    user_id = input("Enter your user ID: ").strip()
    feedback_type = input("Feedback type (bug_report, feature_request, general): ").strip()
    description = input("Describe the issue/feedback: ").strip()

    feedback = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "user_id": user_id,
        "feedback_type": feedback_type,
        "description": description
    }

    save_feedback(feedback)

if __name__ == "__main__":
    print("📋 Feedback Collector")
    print("Type your feedback below...\n")
    collect_feedback()
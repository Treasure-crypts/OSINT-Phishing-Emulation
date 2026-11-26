from email import policy
from email.parser import BytesParser
from pathlib import Path

# Read the sample email
email_file = Path(__file__).resolve().parent.parent / "email-samples" / "sample.eml"

with email_file.open("rb") as file:
    message = BytesParser(policy=policy.default).parse(file)

# Extract email headers
sender = message.get("From", "Not available")
reply_to = message.get("Reply-To", "Not available")
subject = message.get("Subject", "Not available")
authentication = message.get("Authentication-Results")

print("=" * 55)
print("          EMAIL PHISHING INDICATOR ANALYZER")
print("=" * 55)

print("\n[ EMAIL INFORMATION ]")
print("Sender:", sender)
print("Reply-To:", reply_to)
print("Subject:", subject)

print("\n[ SECURITY ANALYSIS ]")

# Check 1: From and Reply-To mismatch
if reply_to != "Not available" and reply_to != sender:
    print("[WARNING] Reply-To address differs from sender.")
else:
    print("[INFO] No obvious Reply-To mismatch detected.")

# Check 2: Urgent subject
urgent_words = ["urgent", "immediately", "action required", "verify"]

if any(word in subject.lower() for word in urgent_words):
    print("[WARNING] Subject contains urgency-related language.")
else:
    print("[INFO] No urgency-related keywords detected.")

# Check 3: Authentication results
if authentication is None:
    print("[INFO] Authentication-Results header unavailable.")
else:
    print("[INFO] Authentication-Results:", authentication)

print("\n[ ANALYSIS COMPLETE ]")
print("=" * 55)

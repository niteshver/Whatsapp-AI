import re
import json
import os
os.makedirs("whatsapp_output", exist_ok=True)


# 1️⃣ Regex pattern
pattern = re.compile(
    r"\d{1,2}/\d{1,2}/\d{2,4},\s*[\d:]+.*?\s*-\s*(.*?):\s*(.*)",
    re.IGNORECASE
)

#/Users/niteshv1520/Whatsapp-AI/whatsapp_ai.py
# 2️⃣ Paths
RAW_FOLDER = os.path.join("raw_chats")

output_dir = "whatsapp_output"
os.makedirs(output_dir, exist_ok=True)

output_data = os.path.join(output_dir, "output_data.json")


all_messages = []

# 3️⃣ Loop through all chat files
for filename in os.listdir(RAW_FOLDER):
    filepath = os.path.join(RAW_FOLDER, filename)

    # ✅ Skip folders and system files
    if not os.path.isfile(filepath):
        continue

    if not filename.endswith(".txt"):
        continue

    print("📂 Reading file:", filename)

    contact = filename.replace(".txt", "")

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.match(line)
            if match:
                sender = match.group(1).strip()
                text = match.group(2).strip()

                all_messages.append({
                    "contact": contact,
                    "sender": sender,
                    "text": text
                })

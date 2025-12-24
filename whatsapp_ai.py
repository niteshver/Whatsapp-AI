import re
import os
import json

RAW_FOLDER = "raw_chats"
OUTPUT_FOLDER = "whatsapp_output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "output_data.json")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

pattern = re.compile(
    r"\d{1,2}/\d{1,2}/\d{2,4}.*?-\s*(.*?):\s*(.*)",
    re.IGNORECASE
)

all_messages = []

for filename in os.listdir(RAW_FOLDER):
    filepath = os.path.join(RAW_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    if not filename.endswith(".txt"):
        continue

    print("📂 Reading file:", filename)

    contact = filename.replace("WhatsApp Chat with ", "").replace(".txt", "").strip()

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.search(line)   # 🔥 IMPORTANT CHANGE
            if match:
                sender = match.group(1).strip()
                message = match.group(2).strip()

                if message:
                    all_messages.append({
                        "contact": contact,
                        "sender": sender,
                        "text": message
                    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_messages, f, ensure_ascii=False, indent=2)

print("✅ TOTAL MESSAGES EXTRACTED:", len(all_messages))

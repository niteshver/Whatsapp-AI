import re
import json
import os
os.makedirs("whatsapp_output", exist_ok=True)


# 1️⃣ Regex pattern
pattern = re.compile(
    r"\d{1,2}/\d{1,2}/\d{2,4}, .* - (.*?): (.*)"
)
#/Users/niteshv1520/Whatsapp-AI/whatsapp_ai.py
# 2️⃣ Paths
raw_data = "/Users/niteshv1520/Desktop/whatsApp_raw_chats"
output_dir = "whatsapp_output"
os.makedirs(output_dir, exist_ok=True)

output_data = os.path.join(output_dir, "output_data.json")


all_messages = []

# 3️⃣ Loop through all chat files
for filename in os.listdir(raw_data):

    if not filename.endswith(".txt"):
        continue

    contact = filename.replace(".txt", "")
    file_path = os.path.join(raw_data, filename)

    # 4️⃣ Read each file
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = pattern.match(line)

            if match:
                sender = match.group(1).strip()
                message = match.group(2).strip()

                all_messages.append({
                    "contact": contact,
                    "sender": sender,
                    "text": message
                })

# 5️⃣ Save JSON output
with open(output_data, "w", encoding="utf-8") as f:
    json.dump(all_messages, f, ensure_ascii=False, indent=2)


print("✅ Chat data extracted successfully")


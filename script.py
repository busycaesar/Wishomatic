import pandas as pd
import datetime
import pywhatkit as kit
import time

# Load CSV file
csv_file = "data.csv"
df = pd.read_csv(csv_file)

# Ensure 'phone_number' is read as a string and strip any extra spaces
df['phone_number'] = df['phone_number'].astype(str).str.strip()

# Get current date in MM-DD format
current_date = datetime.datetime.now().strftime("%m-%d")

# Filter rows with today's month and day
today_wishes = df[df['date'] == current_date]

# Send WhatsApp messages
for _, row in today_wishes.iterrows():
    phone_number = row['phone_number']
    wish_message = row['wish']

    # Add '+' if it's not already present
    if not phone_number.startswith("+"):
        phone_number = "+" + phone_number

    try:
        print(f"Sending message to {phone_number}: {wish_message}")
        kit.sendwhatmsg_instantly(phone_number, wish_message, wait_time=10)
        time.sleep(5)  # Sleep to avoid rate limits
    except Exception as e:
        print(f"Error sending message to {phone_number}: {e}")

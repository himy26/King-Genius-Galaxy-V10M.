import base64
import datetime
import hashlib
import os

SECRET_KEY = "Mohamed_Vision_Prince_2025_Secret" 

def generate_key(days_valid):
    try:
        exp_date = (datetime.date.today() + datetime.timedelta(days=int(days_valid))).strftime("%Y-%m-%d")
        raw_data = f"{exp_date}|{SECRET_KEY}"
        signature = hashlib.md5(raw_data.encode()).hexdigest()[:8]
        token = f"{exp_date}|{signature}"
        encoded_token = base64.b64encode(token.encode()).decode()
        final_key = "VP-" + encoded_token[::-1]
        return final_key, exp_date
    except: return None, None

if __name__ == "__main__":
    print("--- Vision Prince Key Generator ---")
    while True:
        days = input("\nEnter Days (e.g. 365) or 'q': ")
        if days == 'q': break
        key, date = generate_key(int(days))
        print(f"\nKey: {key}\nExpires: {date}\n")
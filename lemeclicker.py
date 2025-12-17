import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

URL = "https://lemehost.com/server/3098476/free_plan?extend_time=1&_pjax=%23p0"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Referer": "https://lemehost.com/server/3098476/free_plan",
    "X-CSRF-Token": "j-7DuRp67GaMHLY25OqSceCwy9BppJeNMiAG4VSgZfjYqLKKckiLMclNzk6DjaQw1dmsgVCX4eoKRHzQGuEHpw==",
    "Cookie": f"advanced-frontend={os.getenv('LEME_ADVANCED_FRONTEND')}; _identity-frontend={os.getenv('LEME_IDENTITY_FRONTEND')};"
}


def extend_time():
    try:
        response = requests.post(URL, headers=HEADERS, timeout=15)

        if response.status_code == 200:
            print("✅ Extend time successful at", time.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print(f"❌ Failed: HTTP {response.status_code}")
    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    print("🚀 Auto Lemehost extender started")
    while True:
        extend_time()
        
        time.sleep(29 * 60)


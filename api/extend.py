import os
import time
import requests
from http.server import BaseHTTPRequestHandler
from dotenv import load_dotenv

load_dotenv()

URL = "https://lemehost.com/server/3098476/free_plan?extend_time=1&_pjax=%23p0"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Referer": "https://lemehost.com/server/3098476/free_plan",
    "X-CSRF-Token": os.environ["LEME_CSRF_TOKEN"],
    "Cookie": (
        f"advanced-frontend={os.environ['LEME_ADVANCED_FRONTEND']}; "
        f"_identity-frontend={os.environ['LEME_IDENTITY_FRONTEND']};"
    ),
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            r = requests.post(URL, headers=HEADERS, timeout=15)

            self.send_response(200 if r.status_code == 200 else 500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                f"Status: {r.status_code} at {time.strftime('%Y-%m-%d %H:%M:%S')}".encode()
            )
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

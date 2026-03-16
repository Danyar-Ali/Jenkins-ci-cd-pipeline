import requests
import time
import sys
import os

URL = os.getenv("TARGET_URL")

def check_site(url):
    start = time.time()

    try:
        response = requests.get(url, timeout = 5)
        latency = time.time() - start

        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        print(f"Response time: {latency:.2f} seconds")

        if response.status_code != 200:
            print("Site returned non-200 status!")
            sys.exit(1)

        if latency > 2:
            print("Site response is too slow!")
            sys.exit(1)


        print("Site health check passed.")


    except Exception as e:
        print("Health check failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    check_site(URL)
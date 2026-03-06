import requests


url = "https://httpbin.org/delay/3"

try:
    responses = requests.get(url, timeout=1)
    responses.raise_for_status()
    print(f"Success :: {responses.json()}")
except requests.exceptions.Timeout:
    print(f" Request Timeout :: {url}")
except requests.exceptions.RequestException as e:
    print(f"Request Failed :: {e} ")

TOKEN = ""
headers = {
    "Authorization" : f"Bearer {TOKEN}"
}

res = requests.get(url, headers= headers)

print(res.json())
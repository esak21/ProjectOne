import requests


url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title" : "Hello From Python",
    "body" : "This is a test post",
    "userId": 1
}

responses = requests.post(url, json=payload)

print(f"Status Code is {responses.status_code}")

data = responses.json()

print(data)


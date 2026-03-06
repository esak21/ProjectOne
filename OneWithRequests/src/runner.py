import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)


print(f"Status Code is :: {response.status_code}")
print(f"Content Type  is :: {response.headers.get("Content-Type")}")


data = response.json()
print(data)



second_url = "https://reqres.in/api/users"
second_url_params = {"page": 2 }

second_response = requests.get(second_url)

print(f"Final URL :: {second_response.url}")

response.raise_for_status()

second_url_data = second_response.json()
print(second_url_data)
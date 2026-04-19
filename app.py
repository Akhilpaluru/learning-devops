import requests

print("Day 9 DevOps 🚀")

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)

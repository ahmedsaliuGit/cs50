import requests

response = requests.get("https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

print(response.json())

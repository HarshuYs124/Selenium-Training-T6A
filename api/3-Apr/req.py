import requests

response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=sold")

print(response)
print(response.status_code)
print(response.text)
print(response.json())
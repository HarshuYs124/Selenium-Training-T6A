import requests
response = requests.get('https://petstore.swagger.io/v2/store/inventory')
expected = 200
actual = response.status_code
assert expected == actual, f"{actual}"

print(response.json()['available'])
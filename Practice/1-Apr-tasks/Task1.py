import requests

payload = {
        "id": 30,
        "name": "doggie",
        "status": "available"
    }
def post():


    response = requests.post("https://petstore.swagger.io/v2/pet", json=payload)

    assert response.status_code == 200, f"Status: {response.status_code}"

    print("POST Response:", response.json())
    return payload["id"]


def get():
    response = requests.get("https://petstore.swagger.io/v2/store/inventory")

    print("Available pets:", response.json().get('available'))
    print("GET Status:", response.status_code)


def delete(pet_id):
    response = requests.delete("https://petstore.swagger.io/v2/pet/{pet_id}")

    print("DELETE Status:", response.status_code)
    print("Response:", response.text)


pet_id = post()
get()
delete(pet_id)
import requests

def post():

    payload = {
        "id":30,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post("https://petstore.swagger.io/v2/pet", json=payload)

    expected = 200
    actual = response.status_code

    assert expected == actual, f"Status: {actual}"

    print(response.json())
    return response.json()

def get():

    response = requests.get("https://petstore.swagger.io/v2/store/inventory")

    res = response.json()

    print(res['available'])
    print(response.status_code)

def delete():

    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    responsee = requests.delete("https://petstore.swagger.io/v2/pet/30")

    print(responsee.status_code)
    # print(responsee.json())
    print(responsee.text)


get()
post()
delete()
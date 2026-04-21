#Task1
import requests
import urllib3
# used to diable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# used to combine all requests to one session
session = requests.Session()

#  Register User
def register():
    payload = {
        "city": "jaipur",
        "country": "India",
        "email": "harshita5@gmail.com",
        "firstName": "Harshita",
        "gender": "FEMALE",
        "lastName": "Yadav",
        "password": "string",
        "phone": 7658006650,
        "state": "Rajasthan",
        "zoneId": "ALPHA"
    }
    # send post request to create user
    response = session.post("https://www.shoppersstack.com/shopping/shoppers", json=payload, verify=False)
    # api response
    print("Register Response:", response.text)
    # check if the response code is correct or not
    expected = 201
    actual = response.status_code
    assert actual == expected, f"Registration failed: {response.status_code}"

    user_id = response.json()['data']['userId']
    return payload['email'], payload["password"], user_id


#  Login
def login(email, password):
    payload = {
        "email": email,
        "password": password,
        "role": "SHOPPER"
    }
    # send post request for login
    response = session.post("https://www.shoppersstack.com/shopping/users/login", json=payload, verify=False)
    print("Login Response:", response.text)
    # check if the response code is valid
    expected=200
    actual=response.status_code
    assert actual == expected, f"Login failed: {response.status_code}"
    # find token
    token = response.json()['data']['jwtToken']
    return token


#  Get User Details
def get_user(user_id, token):
    # used for authentication of token
    headers = {
        "Authorization": f"Bearer {token}"
    }
    # send get request to fetch data
    response = session.get(f"https://www.shoppersstack.com/shopping/shoppers/{user_id}", headers=headers, verify=False)
    print("Get User Response:", response.text)
    # validate response code
    expected = 200
    actual = response.status_code
    assert actual == expected, f"Fetch failed: {response.status_code}"

    print(" User fetched successfully")


#  Flow Execution
email, password, user_id = register()
token = login(email, password)
get_user(user_id, token)
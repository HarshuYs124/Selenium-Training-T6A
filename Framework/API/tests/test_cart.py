from http.client import responses

from api.cart.cart_api import CartApi
from utils.read_data import read_json
from core.auth import get_auth_data

cart_api = CartApi()

def test_AddToCart(auth_data,headers):
    data = read_json("test_data/cart.json")

    details = get_auth_data()
    shopperId = details['shopper_id']

    response = cart_api.  addToCart(shopperId,data,headers=headers)


    assert response.status_code == 201
    print(response.status_code)
    print(response.json())
    print(data)
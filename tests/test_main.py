from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/user/signup",
        headers={"accept":"application/json","Content-Type":"application/json"},
        json={"fullname": "Joe Eric",
              "email": "joe@example.com",
              "password": "Hello123"},
    )
    assert response.status_code == 200

def test_user_login():
    userResponse = client.post(
        "/user/login",
        headers={"accept":"application/json","Content-Type":"application/json"},
        json={"email": "joe@example.com",
              "password": "Hello123"},
    )
    assert userResponse.status_code == 200

def test_get_phone_contry():

    client.post(
        "/user/signup",
        headers={"accept":"application/json",
        "Content-Type":"application/json"},
        json={"fullname": "Joe Eric",
              "email": "joe@example.com",
              "password": "Hello123"},
    )

    userResponse = client.post(
        "/user/login",
        headers={"accept":"application/json",
        "Content-Type":"application/json"},
        json={"email": "joe@example.com",
              "password": "Hello123"},
    )
    response = client.post(
        "/get-phone-country",
        headers={"accept":"application/json",
        "Authorization":"Bearer "+userResponse.json().get('access_token'),
        "Content-Type":"application/json"},
        json={"Phone": "+9199950782734"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "Phone": "+9199950782734",
        "Country": "IN"
    }
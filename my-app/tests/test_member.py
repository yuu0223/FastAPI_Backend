import requests


def test_login():
    url = "http://0.0.0.0:5106/member/login"
    payload = {"email": "Pig@gmail.com", "pwd": "1234"}
    response = requests.post(url, json=payload)

    data = {
        "status": "success",
        "data": {
            "ID": "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2",
            "Name": "Pig",
            "Email": "Pig@gmail.com",
            "Gender": "Male",
        },
    }
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data

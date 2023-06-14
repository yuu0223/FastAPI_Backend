import requests


# login correct
def test_login_correct():
    url = "http://140.119.164.204:5102/member/login"
    payload = {"email": "Pig@gmail.com", "pwd": "4321"}
    response = requests.post(url, json=payload)

    data = {
        "status": "success",
        "data": {
            "ID": "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2",
            "Name": "Pig",
            "Email": "Pig@gmail.com",
            "Gender": "male",
        },
    }
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# login error - 此信箱還沒註冊過
def test_login_error1():
    url = "http://140.119.164.204:5102/member/login"
    payload = {"email": "nothing@gmail.com", "pwd": "0988"}
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "查無此信箱"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# login error - 密碼錯誤
def test_login_error2():
    url = "http://140.119.164.204:5102/member/login"
    payload = {"email": "Pig@gmail.com", "pwd": "0123456"}
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "密碼錯誤，請重新輸入"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# sign up correct
def test_create_member_correct():
    url = "http://140.119.164.204:5102/member/create_member"
    payload = {"name": "Ring", "email": "Ring@gmail.com", "pwd": "1234"}
    response = requests.post(url, json=payload)

    data = {"status": "success", "data": None}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# sign up error - 此信箱已註冊過
def test_create_member_error1():
    url = "http://140.119.164.204:5102/member/create_member"
    payload = {"name": "Ring", "email": "Ring@gmail.com", "pwd": "1234"}
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "此信箱已註冊過，請直接登入，謝謝"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# sign up error - 性別資料型態不正確(None、Female、Male)
def test_create_member_error2():
    url = "http://140.119.164.204:5102/member/create_member"
    payload = {"name": "Ring", "gender": 123, "email": "0123@gmail.com", "pwd": "1234"}
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "性別資料錯誤，請重新檢查唷！"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# update member correct
def test_update_member_correct():
    url = "http://140.119.164.204:5102/member/update_member"
    payload = {
        "account_id": "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2",
        "name": "Pig",
        "gender": "male",
        "pwd": "4321",
    }
    response = requests.patch(url, json=payload)

    data = {"status": "success", "data": None}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# update member error - 查無此帳號
def test_update_member_error1():
    url = "http://140.119.164.204:5102/member/update_member"
    payload = {
        "account_id": "80012345",
        "name": "Pig",
        "gender": "male",
        "pwd": "4321",
    }
    response = requests.patch(url, json=payload)

    data = {"status": "error", "msg": "查無此帳號"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# forget pwd correct
def test_forget_pwd_correct():
    url = "http://140.119.164.204:5102/member/forget_pwd"
    payload = {"email": "Fish@gmail.com"}
    response = requests.patch(url, params=payload)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 8


# forget pwd error - 查無此email
def test_forget_pwd_error1():
    url = "http://140.119.164.204:5102/member/forget_pwd"
    payload = {"email": "yellow@yahoo.com"}
    response = requests.patch(url, params=payload)

    data = {"status": "error", "msg": "查無此信箱資訊，請確認有無輸入錯誤，或是直接註冊～"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data

import requests
import uuid
import datetime


def is_uuid(string):
    try:
        uuid.UUID(string)
        return True
    except ValueError:
        return False


###########
# create_event correct - 建立活動文章
def test_create_event_correct():
    url = "http://140.119.164.204:5102/post/create_event"
    payload = {
        "member_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "type": "活動分享",
        "title": "政大商院演講活動",
        "start_time": "2023-06-25 12:00:00",
        "close_time": "2023-06-20 23:59:00",
        "end_time": "2023-06-30 19:30:00",
        "content": "歡迎報名參加活動！",
        "location": "政大商院1樓",
        "member_num": 50,
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json()["status"] == "success"
    assert is_uuid(response.json()["data"]) == True


# create_event error - 建立活動文章 - 查無此帳號
def test_create_event_error1():
    url = "http://140.119.164.204:5102/post/create_event"
    payload = {
        "member_id": "418ad16f",
        "type": "活動分享",
        "title": "政大商院演講活動",
        "start_time": "2023-06-25 12:00:00",
        "close_time": "2023-06-20 23:59:00",
        "end_time": "2023-06-30 19:30:00",
        "content": "歡迎報名參加活動！",
        "location": "政大商院1樓",
        "member_num": 50,
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "查無此帳號，無法建立活動，請重新登入。"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# create_event error - 建立活動文章 - 前端時間input型態錯誤
def test_create_event_error2():
    url = "http://140.119.164.204:5102/post/create_event"
    payload = {
        "member_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "type": "活動分享",
        "title": "政大商院演講活動",
        "start_time": "2023-06-25",
        "close_time": "2023-06-20",
        "end_time": "2023-06-30",
        "content": "歡迎報名參加活動！",
        "location": "政大商院1樓",
        "member_num": 50,
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 422
    assert response.headers["Content-Type"] == "application/json"


# create_event error - 建立活動文章 - 活動人數<=0
def test_create_event_error3():
    url = "http://140.119.164.204:5102/post/create_event"
    payload = {
        "member_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "type": "活動分享",
        "title": "政大商院演講活動",
        "start_time": "2023-06-25 12:00:00",
        "close_time": "2023-06-20 23:59:00",
        "end_time": "2023-06-30 19:30:00",
        "content": "歡迎報名參加活動！",
        "location": "政大商院1樓",
        "member_num": 0,
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "活動未設定參加人數，請記得填寫唷～"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# create_event error - 建立活動文章 - 活動結束時間早於活動開始時間
def test_create_event_error4():
    url = "http://140.119.164.204:5102/post/create_event"
    payload = {
        "member_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "type": "活動分享",
        "title": "政大商院演講活動",
        "start_time": "2023-06-25 12:00:00",
        "close_time": "2023-06-20 23:59:00",
        "end_time": "2023-05-30 19:30:00",
        "content": "歡迎報名參加活動！",
        "location": "政大商院1樓",
        "member_num": 50,
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "活動結束時間早於活動開始時間，請重新設定"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# create_event error - 建立活動文章 - post type error
def test_create_event_error5():
    url = "http://140.119.164.204:5102/post/create_event"
    payload = {
        "member_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "type": "參加活動",
        "title": "政大商院演講活動",
        "start_time": "2023-06-25 12:00:00",
        "close_time": "2023-06-20 23:59:00",
        "end_time": "2023-05-30 19:30:00",
        "content": "歡迎報名參加活動！",
        "location": "政大商院1樓",
        "member_num": 50,
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "活動類型錯誤，必須為揪團好康、Free Hug、活動分享、禮物贈送。"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


###########
# event_join correct - 參加活動
def test_event_join_correct():
    url = "http://140.119.164.204:5102/post/event_join"
    payload = {
        "member_id": "4ba6c72b-9600-4e8b-a105-dd4cf069c670",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
    }
    response = requests.post(url, json=payload)

    data = {"status": "success", "data": None}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# event_join correct - 參加活動 - 已經報名過了
def test_event_join_error1():
    url = "http://140.119.164.204:5102/post/event_join"
    payload = {
        "member_id": "4ba6c72b-9600-4e8b-a105-dd4cf069c670",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "你已經報名過這個活動囉！是不是迫不及待呀xD"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# event_join correct - 參加活動 - 活動建立者不用報名自己建立的活動
def test_event_join_error2():
    url = "http://140.119.164.204:5102/post/event_join"
    payload = {
        "member_id": "c1c9f9c8-7747-4f74-b934-47e53434fc3a",
        "event_id": "799991aa-12f8-4c7c-aa13-a80e4cdda3e8",
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "你是活動建立者，不用特別報名唷！"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# event_join correct - 參加活動 - 活動已達報名人數上限
def test_event_join_error3():
    url = "http://140.119.164.204:5102/post/event_join"
    payload = {
        "member_id": "bb910b70-c07a-4b59-a38f-3515d526fe92",
        "event_id": "e77c261f-71ad-45e2-8f42-f1a8a3d425d1",
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "活動已達報名人數上限，可以參考看看其他活動唷！"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# event_join correct - 參加活動 - 活動已經結束
def test_event_join_error4():
    url = "http://140.119.164.204:5102/post/event_join"
    payload = {
        "member_id": "4ba6c72b-9600-4e8b-a105-dd4cf069c670",
        "event_id": "19d76913-1631-476a-8492-e84fcdcfe60e",
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "活動已經結束囉"}
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


###########
# member_event_delete correct - 取消參加活動
def test_member_event_delete_correct():
    url = "http://140.119.164.204:5102/post/member_event_delete"
    payload = {
        "member_id": "4ba6c72b-9600-4e8b-a105-dd4cf069c670",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
    }
    response = requests.delete(url, json=payload)

    data = {"status": "success", "data": None}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# member_event_delete error - 取消參加活動 - 查無報名此活動或活動已結束
def test_member_event_delete_error1():
    url = "http://140.119.164.204:5102/post/member_event_delete"
    payload = {
        "member_id": "4ba6c72b-9600-4e8b-a105-dd4cf069c670",
        "event_id": "2170a132-e4bb",
    }
    response = requests.delete(url, json=payload)

    data = {"status": "error", "msg": "你未報名過這個活動或是活動已經結束啦！"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# member_event_delete error - 取消參加活動 - 查無此帳號或系統錯誤不到帳號
def test_member_event_delete_error2():
    url = "http://140.119.164.204:5102/post/member_event_delete"
    payload = {
        "member_id": "4ba6c72b-9600",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
    }
    response = requests.delete(url, json=payload)

    data = {"status": "error", "msg": "查無此帳號或系統錯誤，請與相關人員聯絡～謝謝"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


###########
# contact_poster correct - 寄信詢問發文者
def test_contact_poster_correct():
    url = "http://140.119.164.204:5102/post/contact_poster"
    payload = {
        "member_id": "4ba6c72b-9600-4e8b-a105-dd4cf069c670",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
        "title": "string test",
        "content": "string",
    }
    response = requests.post(url, json=payload)

    data = {
        "status": "success",
        "data": {
            "member_name": "Cow",
            "member_email": "Cow@gmail.com",
            "poster_name": "Dog",
            "poster_email": "Dog@gmail.com",
            "email_title": "string test",
            "email_content": "string",
        },
    }

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# contact_poster error - 寄信詢問發文者 - 使用者未登入
def test_contact_poster_error1():
    url = "http://140.119.164.204:5102/post/contact_poster"
    payload = {
        "member_id": "None",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
        "title": "string test",
        "content": "string",
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "尚未登入或查無此帳號，請重新登入。"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# contact_poster error - 寄信詢問發文者 - 查無活動
def test_contact_poster_error2():
    url = "http://140.119.164.204:5102/post/contact_poster"
    payload = {
        "member_id": "4ba6c72b-9600-4e8b-a105-dd4cf069c670",
        "event_id": "2170a1",
        "title": "string test",
        "content": "string",
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "查無活動，請確認活動是否存在。"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# contact_poster error - 寄信詢問發文者 - 發文者本人不用寄信給自己
def test_contact_poster_error3():
    url = "http://140.119.164.204:5102/post/contact_poster"
    payload = {
        "member_id": "bb910b70-c07a-4b59-a38f-3515d526fe92",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
        "title": "string test",
        "content": "string",
    }
    response = requests.post(url, json=payload)

    data = {"status": "error", "msg": "這是你建立的活動唷！"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


###########
# get_event_info correct - 活動詳細內容
def test_get_event_info_correct():
    url = "http://140.119.164.204:5102/post/event_info"
    payload = {"event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3"}
    response = requests.get(url, params=payload)

    data = {
        "status": "success",
        "data": [
            {
                "title": "五月天演唱會門票免費贈送",
                "type": "禮物贈送",
                "name": "Dog",
                "start_time": "2023-05-25 09:42:34",
                "close_time": "2023-06-28 09:42:34",
                "end_time": "2023-06-29 09:42:34",
                "content": "目前有多出4張五月天門票，想贈送給大家~歡迎索取",
                "event_limit": 4,
                "account_id": "bb910b70-c07a-4b59-a38f-3515d526fe92",
                "email": "Dog@gmail.com",
            }
        ],
    }

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# get_event_info error - 活動詳細內容 - 查無此文章
def test_get_event_info_error1():
    url = "http://140.119.164.204:5102/post/event_info"
    payload = {"event_id": "aaa1234"}
    response = requests.get(url, params=payload)

    data = {"status": "error", "msg": "查無此文章，可能已遭刪除。"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


###########
# get_member_event_join correct - 使用者查詢個人參加之活動列表
def test_get_member_event_join_correct():
    url = "http://140.119.164.204:5102/post/member_event_join"
    payload = {"member_id": "418ad16f-859d-4939-bc4b-2c43f020c56a"}
    response = requests.get(url, params=payload)

    data = {
        "status": "success",
        "data": [
            {
                "ID": "17316a7c-0751-4e37-bdca-a514cb46d9eb",
                "title": "游泳課三人同行一人免費",
                "type": "活動分享",
                "is_closed": False,
            },
            {
                "ID": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
                "title": "五月天演唱會門票免費贈送",
                "type": "禮物贈送",
                "is_closed": False,
            },
        ],
    }

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# ###########
# poster_cancel_post correct - 發文者取消(關閉)文章
def test_poster_cancel_post_correct():
    url = "http://140.119.164.204:5102/post/cancel_post"
    payload = {
        "member_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "event_id": "e77c261f-71ad-45e2-8f42-f1a8a3d425d1",
    }
    response = requests.delete(url, json=payload)

    data = {"status": "success", "data": None}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# poster_cancel_post error - 發文者取消(關閉)文章 - 活動時間已截止
def test_poster_cancel_post_error1():
    url = "http://140.119.164.204:5102/post/cancel_post"
    payload = {
        "member_id": "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2",
        "event_id": "17316a7c-0751-4e37-bdca-a514cb46d9eb",
    }
    response = requests.delete(url, json=payload)

    data = {"status": "error", "msg": "活動已經關閉囉"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# poster_cancel_post error - 發文者取消(關閉)文章 - 非活動發起人
def test_poster_cancel_post_error2():
    url = "http://140.119.164.204:5102/post/cancel_post"
    payload = {
        "member_id": "ab0b88f6-2",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
    }
    response = requests.delete(url, json=payload)

    data = {"status": "error", "msg": "你不是活動建立者，不能取消活動唷！"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# ###########
# get_member_event correct - user為poster建立之活動列表
def test_get_member_event_correct1():
    url = "http://140.119.164.204:5102/post/member_event"
    payload = {
        "member_id": "28f70987-c209-43db-8fa6-f716c5568388",
    }
    response = requests.get(url, params=payload)

    data = {"status": "success", "data": []}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# get_member_event correct - user為poster建立之活動列表
def test_get_member_event_correct2():
    url = "http://140.119.164.204:5102/post/member_event"
    payload = {
        "member_id": "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2",
    }
    response = requests.get(url, params=payload)

    data = {
        "status": "success",
        "data": [
            {
                "ID": "17316a7c-0751-4e37-bdca-a514cb46d9eb",
                "poster_id": "ab0b88f6-8d4c-4098-ae7c-599c87c7a1f2",
                "type": "活動分享",
                "title": "游泳課三人同行一人免費",
                "content": "政大游泳系開課啦～凡是政大學生揪團報名課程，三人同行一人免費，一個人只要999!",
                "location": "政大池塘",
                "limit_member": 3,
                "create_time": "2023-05-25 09:42:34",
                "start_time": "2023-05-25 09:42:34",
                "end_time": "2023-06-29 09:42:34",
                "close_time": "2023-05-13 22:40:23",
            }
        ],
    }
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# get_member_event error - user為poster建立之活動列表 - 查無此帳號
def test_get_member_event_error1():
    url = "http://140.119.164.204:5102/post/member_event"
    payload = {
        "member_id": "228787f1",
    }
    response = requests.get(url, params=payload)

    data = {"status": "error", "msg": "查無此帳號，請重新登入唷！"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# ###########
# get_member_event_info correct - poster查詢活動詳細內容
def test_get_member_event_info_correct():
    url = "http://140.119.164.204:5102/post/member_event_info"
    payload = {
        "member_id": "bb910b70-c07a-4b59-a38f-3515d526fe92",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
    }
    response = requests.get(url, params=payload)

    data = {
        "status": "success",
        "data": {
            "title": "五月天演唱會門票免費贈送",
            "type": "禮物贈送",
            "name": "Dog",
            "start_time": "2023-05-25 09:42:34",
            "close_time": "2023-06-28 09:42:34",
            "end_time": "2023-06-29 09:42:34",
            "content": "目前有多出4張五月天門票，想贈送給大家~歡迎索取",
            "event_limit": 4,
            "account_id": "bb910b70-c07a-4b59-a38f-3515d526fe92",
            "email": "Dog@gmail.com",
            "post_participant": [
                {
                    "account_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
                    "name": "Apple",
                    "email": "Apple@gmail.com",
                    "gender": "female",
                },
                {
                    "account_id": "c1c9f9c8-7747-4f74-b934-47e53434fc3a",
                    "name": "Fish",
                    "email": "Fish@gmail.com",
                    "gender": "female",
                },
            ],
        },
    }

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# get_member_event_info error - poster查詢活動詳細內容 - 不是發文者不得查詢
def test_get_member_event_info_error1():
    url = "http://140.119.164.204:5102/post/member_event_info"
    payload = {
        "member_id": "bb910b70",
        "event_id": "2170a132-e4bb-4c0c-8d01-05b7cfb2a2e3",
    }
    response = requests.get(url, params=payload)

    data = {"status": "error", "msg": "此活動不是你建立的唷！"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# ###########
# update_event_info correct - poster修改活動詳細內容
def test_update_event_info_correct():
    url = "http://140.119.164.204:5102/post/update_event_info"
    payload = {
        "event_id": "e77c261f-71ad-45e2-8f42-f1a8a3d425d1",
        "acount_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "title": "string",
        "content": "string",
        "location": "string",
        "type": "string",
        "start_time": "2023-06-25T13:10:29.593Z",
        "end_time": "2023-06-30T13:10:29.593Z",
        "close_time": "2023-06-20T13:10:29.593Z",
        "member_num": 0,
    }
    response = requests.patch(url, json=payload)

    data = {"status": "success", "data": None}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# update_event_info error - poster修改活動詳細內容 - 查無此帳號
def test_update_event_info_error1():
    url = "http://140.119.164.204:5102/post/update_event_info"
    payload = {
        "event_id": "e77c261f-71ad-45e2-8f42-f1a8a3d425d1",
        "acount_id": "bc4b-2c43f020c56a",
        "title": "string",
        "content": "string",
        "location": "string",
        "type": "string",
        "start_time": "2023-06-25T13:10:29.593Z",
        "end_time": "2023-06-30T13:10:29.593Z",
        "close_time": "2023-06-20T13:10:29.593Z",
        "member_num": 1,
    }
    response = requests.patch(url, json=payload)

    data = {"status": "error", "msg": "查無此帳號，請重新登入！"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# update_event_info error - poster修改活動詳細內容 - 非發文者不得修改文章
def test_update_event_info_error2():
    url = "http://140.119.164.204:5102/post/update_event_info"
    payload = {
        "event_id": "e77c261f-71ad-45e2-8f42-f1a8a3d425d1",
        "acount_id": "bb910b70-c07a-4b59-a38f-3515d526fe92",
        "title": "string",
        "content": "string",
        "location": "string",
        "type": "string",
        "start_time": "2023-06-25T13:10:29.593Z",
        "end_time": "2023-06-30T13:10:29.593Z",
        "close_time": "2023-06-20T13:10:29.593Z",
        "member_num": 1,
    }
    response = requests.patch(url, json=payload)

    data = {"status": "error", "msg": "你不是這篇文章的發文者，不能修改！"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# update_event_info error - poster修改活動詳細內容 - 活動時間早於開始時間
def test_update_event_info_error3():
    url = "http://140.119.164.204:5102/post/update_event_info"
    payload = {
        "event_id": "e77c261f-71ad-45e2-8f42-f1a8a3d425d1",
        "acount_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "title": "string",
        "content": "string",
        "location": "string",
        "type": "string",
        "start_time": "2023-06-25T13:10:29.593Z",
        "end_time": "2023-06-01T13:10:29.593Z",
        "close_time": "2023-06-20T13:10:29.593Z",
        "member_num": 1,
    }
    response = requests.patch(url, json=payload)

    data = {"status": "error", "msg": "活動結束時間早於活動開始時間，請重新設定"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data


# update_event_info error - poster修改活動詳細內容 - 查無此活動
def test_update_event_info_error4():
    url = "http://140.119.164.204:5102/post/update_event_info"
    payload = {
        "event_id": "e77c261f-71ad",
        "acount_id": "418ad16f-859d-4939-bc4b-2c43f020c56a",
        "title": "string",
        "content": "string",
        "location": "string",
        "type": "string",
        "start_time": "2023-06-25T13:10:29.593Z",
        "end_time": "2023-06-30T13:10:29.593Z",
        "close_time": "2023-06-02T13:10:29.593Z",
        "member_num": 1,
    }
    response = requests.patch(url, json=payload)

    data = {"status": "error", "msg": "查無此活動資訊"}

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == data

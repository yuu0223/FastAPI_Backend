from services.post import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response
import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
post_type = ["揪團好康", "Free Hug", "禮物贈送", "活動分享"]


# 活動建立
async def create_event(
    uuid_code, CreateEventRequest: schema.CreateEventRequest, db: Session
):
    account_info = await crud.get_account_info_by_id(CreateEventRequest.member_id, db)

    if not account_info:
        return Response.Error(msg="查無此帳號，無法建立活動，請重新登入。")

    if CreateEventRequest.type not in post_type:
        return Response.Error(msg="活動類型錯誤，必須為揪團好康、Free Hug、活動分享、禮物贈送。")

    if CreateEventRequest.end_time < CreateEventRequest.start_time:
        return Response.Error(msg="活動結束時間早於活動開始時間，請重新設定")

    if CreateEventRequest.member_num <= 0:
        return Response.Error(msg="活動未設定參加人數，請記得填寫唷～")

    CreateEventRequest.start_time = (
        datetime.datetime.strftime(
            CreateEventRequest.start_time + datetime.timedelta(hours=8), DATETIME_FORMAT
        )
        if CreateEventRequest.start_time is not None
        else CreateEventRequest.start_time
    )
    CreateEventRequest.close_time = (
        datetime.datetime.strftime(
            CreateEventRequest.close_time + datetime.timedelta(hours=8), DATETIME_FORMAT
        )
        if CreateEventRequest.close_time is not None
        else CreateEventRequest.close_time
    )
    CreateEventRequest.end_time = (
        datetime.datetime.strftime(
            CreateEventRequest.end_time + datetime.timedelta(hours=8), DATETIME_FORMAT
        )
        if CreateEventRequest.end_time is not None
        else CreateEventRequest.end_time
    )

    await crud.create_event(uuid_code, CreateEventRequest, db)
    return Response.Success(data=uuid_code)


# 取得活動資訊
async def get_event_info(event_id: str, db: Session):
    event_info = await crud.get_event_info_by_id(event_id, db)

    if not event_info:
        return Response.Error(msg="查無此文章，可能已遭刪除。")

    # 轉換成正確的時間型態
    event_info[0]["start_time"] = datetime.datetime.strftime(
        event_info[0]["start_time"], DATETIME_FORMAT) if event_info[0]["start_time"] is not None else event_info[0]["start_time"]
    event_info[0]["close_time"] = datetime.datetime.strftime(
        event_info[0]["close_time"], DATETIME_FORMAT) if event_info[0]["close_time"] is not None else event_info[0]["close_time"]
    event_info[0]["end_time"] = datetime.datetime.strftime(
        event_info[0]["end_time"], DATETIME_FORMAT) if event_info[0]["end_time"] is not None else event_info[0]["end_time"]

    return Response.Success(data=event_info)


# 參與活動
async def event_join(EventJoinRequest: schema.EventJoinRequest, db: Session):
    event_info = await crud.get_event_info_by_id(EventJoinRequest.event_id, db)
    event_member = await crud.event_member(EventJoinRequest.event_id, db)

    if event_info[0]["end_time"] < datetime.datetime.now():
        return Response.Error(msg="活動已經結束囉")

    if len(event_member)+1 > event_info[0]["event_limit"]:
        return Response.Error(msg="活動已達報名人數上限，可以參考看看其他活動唷！")

    if event_info[0]["account_id"] == EventJoinRequest.member_id:
        return Response.Error(msg="你是活動建立者，不用特別報名唷！")

    if EventJoinRequest.member_id in event_member:
        return Response.Error(msg="你已經報名過這個活動囉！是不是迫不及待呀xD")

    await crud.event_join(EventJoinRequest, db)
    return Response.Success(data=None)


# 寄信給發文者
async def contact_poster(EmailPosterRequest: schema.EmailPosterRequest, db: Session):
    event_info = await crud.get_event_info_by_id(EmailPosterRequest.event_id, db)
<<<<<<< Updated upstream
    user_mail_info = {"member_id": EmailPosterRequest.member_id,
                      "poster_name": event_info[0]["name"],
                      "poster_email": event_info[0]["email"],
                      "email_title": EmailPosterRequest.title,
                      "email_content": EmailPosterRequest.content}
=======
    account_info = await crud.get_account_info_detail_by_id(
        EmailPosterRequest.member_id, db
    )
>>>>>>> Stashed changes

    if event_info and account_info:
        if account_info["Email"] != event_info[0]["email"]:
            user_mail_info = {
                "member_name": account_info["Name"],
                "member_email": account_info["Email"],
                "poster_name": event_info[0]["name"],
                "poster_email": event_info[0]["email"],
                "email_title": EmailPosterRequest.title,
                "email_content": EmailPosterRequest.content,
            }

            return Response.Success(data=user_mail_info)
        else:
            return Response.Error(msg="這是你建立的活動唷！")

    elif not account_info:
        return Response.Error(msg="尚未登入或查無此帳號，請重新登入。")

    elif not event_info:
        return Response.Error(msg="查無活動，請確認活動是否存在。")


# 取得活動文章列表
async def get_event_list(id, time, db: Session):
    event_list = await crud.get_event_list(id, time, db)

    return Response.Success(data=event_list)
<<<<<<< Updated upstream
=======


# 使用者活動列表
async def get_member_event_join(member_id: str, db: Session):
    member_event_join = await crud.get_member_event_join(member_id, db)

    return Response.Success(data=member_event_join)


# 刪除使用者參與之活動
async def delete_member_event_join(
    DeleteMemberEventJoinRequest: schema.DeleteMemberEventJoinRequest, db: Session
):
    member_exist = await crud.get_account_info_by_id(
        DeleteMemberEventJoinRequest.member_id, db
    )

    if member_exist:
        member_event_join = await crud.get_member_event_join(
            DeleteMemberEventJoinRequest.member_id, db
        )
        event_id_list = [
            item["ID"] for item in member_event_join if not item["is_closed"]
        ]

        if DeleteMemberEventJoinRequest.event_id not in event_id_list:
            return Response.Error(msg="你未報名過這個活動或是活動已經結束啦！")
        else:
            await crud.delete_member_event_join(DeleteMemberEventJoinRequest, db)
            return Response.Success(data=None)
    else:
        return Response.Error(msg="查無此帳號或系統錯誤，請與相關人員聯絡～謝謝")


# 發文者取消(關閉)自己發的文
async def poster_cancel_post(CancelPostRequest: schema.CancelPostRequest, db: Session):
    event_info = await crud.get_event_info_by_id(CancelPostRequest.event_id, db)

    if event_info[0]["close_time"] <= datetime.datetime.now():
        return Response.Error(msg="活動已經關閉囉")

    if event_info[0]["account_id"] != CancelPostRequest.member_id:
        return Response.Error(msg="你不是活動建立者，不能取消活動唷！")

    await crud.poster_cancel_post(CancelPostRequest, db)
    return Response.Success(data=None)


async def get_member_event(member_id: str, db: Session):
    member_info = await crud.get_account_info_by_id(member_id, db)

    if member_info:
        member_event = await crud.get_member_event(member_id, db)

        if len(member_event) == 0:
            member_event = []

        return Response.Success(data=member_event)
    else:
        return Response.Error(msg="查無此帳號，請重新登入唷！")


async def get_member_event_info(member_id: str, event_id: str, db: Session):
    event_info = await crud.get_event_info_by_id(event_id, db)
    event_info[0]["start_time"] = datetime.datetime.strftime(
        event_info[0]["start_time"], DATETIME_FORMAT
    )
    event_info[0]["close_time"] = datetime.datetime.strftime(
        event_info[0]["close_time"], DATETIME_FORMAT
    )
    event_info[0]["end_time"] = datetime.datetime.strftime(
        event_info[0]["end_time"], DATETIME_FORMAT
    )
    if member_id != event_info[0]["account_id"]:
        return Response.Error(msg="此活動不是你建立的唷！")

    post_participant = await crud.get_post_participant_by_event_id(event_id, db)
    member_event_info = event_info[0]
    member_event_info.update({"post_participant": post_participant})

    return Response.Success(data=member_event_info)


# 更新文章內容
async def update_event(UpdateEventRequest: schema.UpdateEventRequest, db: Session):
    account_info = await crud.get_account_info_by_id(UpdateEventRequest.acount_id, db)
    event_info = await crud.get_event_info_by_id(UpdateEventRequest.event_id, db)

    if event_info and account_info:
        if account_info["ID"] != event_info[0]["account_id"]:
            return Response.Error(msg="你不是這篇文章的發文者，不能修改！")

        elif UpdateEventRequest.end_time < UpdateEventRequest.start_time:
            return Response.Error(msg="活動結束時間早於活動開始時間，請重新設定")
        else:
            await crud.update_event(UpdateEventRequest, db)
            return Response.Success(data=None)

    elif not event_info:
        return Response.Error(msg="查無此活動資訊")

    elif not account_info:
        return Response.Error(msg="查無此帳號，請重新登入！")
>>>>>>> Stashed changes

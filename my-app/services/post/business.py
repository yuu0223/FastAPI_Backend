from services.post import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response
import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


# 活動建立
async def create_event(uuid_code, CreateEventRequest: schema.CreateEventRequest, db: Session):

    account_info = await crud.get_account_info_by_id(CreateEventRequest.member_id, db)

    if not account_info:
        return Response.Error(msg="查無此帳號，無法建立活動，請重新登入。")

    if CreateEventRequest.end_time < CreateEventRequest.start_time:
        return Response.Error(msg="活動結束時間早於活動開始時間，請重新設定")

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

    if event_info[0]["start_time"] > datetime.datetime.now():
        return Response.Error(msg="活動尚未開始")

    if event_info[0]["end_time"] < datetime.datetime.now():
        return Response.Error(msg="活動已經結束囉")

    if len(event_member)+1 > event_info[0]["event_limit"]:
        return Response.Error(msg="活動已達報名人數上限，可以參考看看其他活動唷！")

    if EventJoinRequest.member_id in event_member:
        return Response.Error(msg="你已經報名過這個活動囉！是不是迫不及待呀xD")

    if event_info[0]["account_id"] == EventJoinRequest.member_id:
        return Response.Error(msg="你是活動建立者，不用特別報名唷！")

    await crud.event_join(EventJoinRequest, db)
    return Response.Success(data=None)


# 寄信給發文者
async def contact_poster(EmailPosterRequest: schema.EmailPosterRequest, db: Session):

    event_info = await crud.get_event_info_by_id(EmailPosterRequest.event_id, db)
    user_mail_info = {"member_id": EmailPosterRequest.member_id,
                      "poster_name": event_info[0]["name"],
                      "poster_email": event_info[0]["email"],
                      "email_title": EmailPosterRequest.title,
                      "email_content": EmailPosterRequest.content}

    return Response.Success(data=user_mail_info)


# 取得活動文章列表
async def get_event_list(time, db: Session):

    event_list = await crud.get_event_list(time, db)

    return Response.Success(data=event_list)

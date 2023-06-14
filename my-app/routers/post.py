from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.post import business, schema
import uuid
import datetime

router = APIRouter(prefix="/post", tags=["post"])


@router.post("/create_event", summary="活動建立")
async def create_event(
    CreateEventRequest: schema.CreateEventRequest, db: Session = Depends(get_db)
):
    uuid_code = str(uuid.uuid4())
    return await business.create_event(uuid_code, CreateEventRequest, db)


@router.post("/event_join", summary="參加活動")
async def event_join(
    EventJoinRequest: schema.EventJoinRequest, db: Session = Depends(get_db)
):
    return await business.event_join(EventJoinRequest, db)


@router.post("/contact_poster", summary="寄信詢問發文者")
async def contact_poster(
    EmailPosterRequest: schema.EmailPosterRequest, db: Session = Depends(get_db)
):
    return await business.contact_poster(EmailPosterRequest, db)


##沒測試
@router.get("/event_list", summary="首頁活動列表")
async def get_event_list(
    id: str, time: datetime.datetime, db: Session = Depends(get_db)
):
    return await business.get_event_list(id, time, db)


@router.get("/event_info", summary="活動詳細內容")
async def get_event_info(event_id: str, db: Session = Depends(get_db)):
    return await business.get_event_info(event_id, db)
<<<<<<< Updated upstream
=======


@router.get("/member_event_join", summary="使用者查詢個人參加之活動列表")
async def get_member_event_join(member_id: str, db: Session = Depends(get_db)):
    return await business.get_member_event_join(member_id, db)


@router.delete("/member_event_delete", summary="使用者取消參與之活動")
async def delete_member_event_join(
    DeleteMemberEventJoinRequest: schema.DeleteMemberEventJoinRequest,
    db: Session = Depends(get_db),
):
    return await business.delete_member_event_join(DeleteMemberEventJoinRequest, db)


@router.delete("/cancel_post", summary="發文者取消(關閉)文章")
async def poster_cancel_post(
    CancelPostRequest: schema.CancelPostRequest, db: Session = Depends(get_db)
):
    return await business.poster_cancel_post(CancelPostRequest, db)


@router.get("/member_event", summary="使用者建立之活動列表")
async def get_member_event(member_id: str, db: Session = Depends(get_db)):
    return await business.get_member_event(member_id, db)


@router.get("/member_event_info", summary="使用者建立之活動詳細內容")
async def get_member_event_info(
    member_id: str, event_id: str, db: Session = Depends(get_db)
):
    return await business.get_member_event_info(member_id, event_id, db)


@router.patch("/update_event_info", summary="更新文章內容")
async def update_event_info(
    UpdateEventRequest: schema.UpdateEventRequest, db: Session = Depends(get_db)
):
    return await business.update_event(UpdateEventRequest, db)
>>>>>>> Stashed changes

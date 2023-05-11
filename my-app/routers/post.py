from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.post import business, schema
import uuid
import datetime

router = APIRouter(prefix="/post", tags=["post"])


@router.post("/create_event", summary="活動建立")
async def create_event(CreateEventRequest: schema.CreateEventRequest, db: Session = Depends(get_db)):

    uuid_code = str(uuid.uuid4())
    return await business.create_event(uuid_code, CreateEventRequest, db)


@router.post("/event_join", summary="參加活動")
async def event_join(EventJoinRequest: schema.EventJoinRequest, db: Session = Depends(get_db)):

    return await business.event_join(EventJoinRequest, db)


@router.post("/contact_poster", summary="寄信詢問發文者")
async def contact_poster(EmailPosterRequest: schema.EmailPosterRequest, db: Session = Depends(get_db)):

    return await business.contact_poster(EmailPosterRequest, db)


@router.get("/event_list", summary="首頁活動列表")
async def get_event_list(time: datetime.datetime, db: Session = Depends(get_db)):

    return await business.get_event_list(time, db)


@router.get("/event_info", summary="活動詳細內容")
async def get_event_info(event_id: str, db: Session = Depends(get_db)):

    return await business.get_event_info(event_id, db)

import re
import datetime
from pydantic.main import BaseModel


class CreateEventRequest(BaseModel):
    member_id: str
    type: str
    title: str
    start_time: datetime.datetime
    close_time: datetime.datetime
    end_time: datetime.datetime
    content: str
    location: str
    member_num: int


class EventJoinRequest(BaseModel):
    member_id: str
    event_id: str


class EmailPosterRequest(BaseModel):
    member_id: str
    event_id: str
    title: str
    content: str
<<<<<<< Updated upstream
=======


class DeleteMemberEventJoinRequest(BaseModel):
    member_id: str
    event_id: str


class CancelPostRequest(BaseModel):
    member_id: str
    event_id: str


class UpdateEventRequest(BaseModel):
    event_id: str
    acount_id: str
    title: str
    content: str
    location: str
    type: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    close_time: datetime.datetime
    member_num: int
>>>>>>> Stashed changes

from utils.db_model import Account, Post, PostParticipant
from sqlalchemy.orm.session import Session
from services.post import schema
from sqlalchemy.sql.functions import func
import datetime


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


async def get_account_info_by_id(account_id: str, db: Session):

    account_info = [
        {
            "ID": data[0]
        }
        for data in db.query(
            Account.ID
        )
        .filter(Account.ID == account_id)
        .all()
    ]

    if len(account_info) > 0:
        return account_info[0]
    else:
        return None


async def create_event(uuid_code, postRequest: schema.CreateEventRequest, db: Session):

    db.add(
        Post(
            ID=uuid_code,
            Account_id=postRequest.member_id,
            Type=postRequest.type,
            Title=postRequest.title,
            Create_time=datetime.datetime.now(),
            Start_time=datetime.datetime.strftime(
                postRequest.start_time, DATETIME_FORMAT) if postRequest.start_time is not None else postRequest.start_time,
            Close_time=datetime.datetime.strftime(
                postRequest.close_time, DATETIME_FORMAT) if postRequest.close_time is not None else postRequest.close_time,
            End_time=datetime.datetime.strftime(
                postRequest.end_time, DATETIME_FORMAT) if postRequest.end_time is not None else postRequest.end_time,
            Content=postRequest.content,
            Location=postRequest.location,
            Limit_member=postRequest.member_num
        )
    )
    db.commit()


async def get_event_info_by_id(event_id: str, db: Session):

    event_info = [
        {
            "title": data[0],
            "type": data[1],
            "name": data[2],
            "start_time": data[3],
            "close_time": data[4],
            "end_time": data[5],
            "content": data[6],
            "event_limit": data[7],
            "account_id": data[8],
            "email": data[9]
        }
        for data in db.query(
            Post.Title,
            Post.Type,
            Account.Name,
            Post.Start_time,
            Post.Close_time,
            Post.End_time,
            Post.Content,
            Post.Limit_member,
            Post.Account_id,
            Account.Email
        )
        .join(Account, Post.Account_id == Account.ID)
        .filter(Post.ID == event_id)  # SQL where
        .all()
    ]
    return event_info


async def event_member(event_id: str, db: Session):

    event_member = [data[0] for data in db.query(
        PostParticipant.Account_id).filter(PostParticipant.Post_id == event_id).all()]

    return event_member


async def event_join(postRequest: schema.EventJoinRequest, db: Session):

    db.add(
        PostParticipant(
            Account_id=postRequest.member_id,
            Post_id=postRequest.event_id
        )
    )
    db.commit()


async def get_event_list(time, db: Session):

    event_info = [
        {
            "ID": data[0],
            "title": data[1],
            "type": data[2],
            "start_time": datetime.datetime.strftime(data[3], DATETIME_FORMAT) if data[3] is not None else data[3]
        }
        for data in db.query(
            Post.ID,
            Post.Title,
            Post.Type,
            Post.Start_time
        )
        .filter(Post.Close_time > datetime.datetime.now(), Post.Close_time > time)
        .order_by(Post.Close_time.asc())
        .limit(5)
        .all()
    ]

    return event_info

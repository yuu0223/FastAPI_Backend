from utils.db_model import Account, Post, PostParticipant
from sqlalchemy.orm.session import Session
from services.post import schema
import datetime


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


async def get_account_info_by_id(account_id: str, db: Session):

    account_info = [{"ID": data[0]} for data in db.query(Account.ID).filter(Account.ID == account_id).all()]

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
            Start_time=postRequest.start_time,
            Close_time=postRequest.close_time,
            End_time=postRequest.end_time,
            Content=postRequest.content,
            Location=postRequest.location,
            Limit_member=postRequest.member_num,
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
            "email": data[9],
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
            Account.Email,
        )
        .join(Account, Post.Account_id == Account.ID)
        .filter(Post.ID == event_id)  # SQL where
        .all()
    ]
    return event_info


async def event_member(event_id: str, db: Session):

    event_member = [
        data[0] for data in db.query(PostParticipant.Account_id).filter(PostParticipant.Post_id == event_id).all()
    ]

    return event_member


async def event_join(postRequest: schema.EventJoinRequest, db: Session):

    db.add(PostParticipant(Account_id=postRequest.member_id, Post_id=postRequest.event_id))
    db.commit()


async def get_event_list(time, db: Session):

    event_info = [
        {
            "ID": data[0],
            "title": data[1],
            "type": data[2],
            "start_time": datetime.datetime.strftime(data[3], DATETIME_FORMAT) if data[3] is not None else data[3],
        }
        for data in db.query(Post.ID, Post.Title, Post.Type, Post.Start_time)
        .filter(Post.Close_time > datetime.datetime.now(), Post.Close_time > time)
        .order_by(Post.Close_time.asc())
        .limit(5)
        .all()
    ]

    return event_info


async def get_member_event_join(member_id: str, db: Session):
    # 找出該會員參與之活動，並判斷該活動是否已結束
    member_event_join = [
        {
            "ID": data[0],
            "title": data[1],
            "type": data[2],
            "is_closed": True if data[3] <= datetime.datetime.now() else False,
        }
        for data in db.query(Post.ID, Post.Title, Post.Type, Post.End_time)
        .join(PostParticipant, Post.ID == PostParticipant.Post_id)
        .filter(PostParticipant.Account_id == member_id)
        .all()
    ]

    return member_event_join


async def delete_member_event_join(DeleteMemberEventJoinRequest: schema.DeleteMemberEventJoinRequest, db: Session):

    db.query(PostParticipant).filter(
        PostParticipant.Account_id == DeleteMemberEventJoinRequest.member_id,
        PostParticipant.Post_id == DeleteMemberEventJoinRequest.event_id,
    ).delete()
    db.commit()

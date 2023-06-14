from utils.db_model import Account, Post, PostParticipant
from sqlalchemy.orm.session import Session
from services.post import schema
from sqlalchemy.sql.functions import func
import datetime


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


async def get_account_info_by_id(account_id: str, db: Session):
    account_info = [
        {"ID": data[0]}
        for data in db.query(Account.ID).filter(Account.ID == account_id).all()
    ]

<<<<<<< Updated upstream
    account_info = [
        {
            "ID": data[0]
        }
        for data in db.query(
            Account.ID
        )
=======
    if len(account_info) > 0:
        return account_info[0]
    else:
        return None


async def get_account_info_detail_by_id(account_id: str, db: Session):
    account_info = [
        {"ID": data[0], "Email": data[1], "Name": data[2]}
        for data in db.query(Account.ID, Account.Email, Account.Name)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream

    event_member = [data[0] for data in db.query(
        PostParticipant.Account_id).filter(PostParticipant.Post_id == event_id).all()]
=======
    event_member = [
        data[0]
        for data in db.query(PostParticipant.Account_id)
        .filter(PostParticipant.Post_id == event_id)
        .all()
    ]
>>>>>>> Stashed changes

    return event_member


async def event_join(postRequest: schema.EventJoinRequest, db: Session):
<<<<<<< Updated upstream

    db.add(
        PostParticipant(
            Account_id=postRequest.member_id,
            Post_id=postRequest.event_id
        )
=======
    db.add(
        PostParticipant(Account_id=postRequest.member_id, Post_id=postRequest.event_id)
>>>>>>> Stashed changes
    )
    db.commit()


async def get_event_list(id, time, db: Session):
    event_info = [
        {
            "ID": data[0],
            "poster_id": data[1],
            "type": data[2],
<<<<<<< Updated upstream
            "start_time": datetime.datetime.strftime(data[3], DATETIME_FORMAT) if data[3] is not None else data[3]
        }
        for data in db.query(
            Post.ID,
            Post.Title,
            Post.Type,
            Post.Start_time
        )
        .filter(Post.Close_time > datetime.datetime.now(), Post.Close_time > time)
=======
            "title": data[3],
            "content": data[4],
            "location": data[5],
            "limit_member": data[6],
            "create_time": datetime.datetime.strftime(data[7], DATETIME_FORMAT)
            if data[7] is not None
            else data[7],
            "start_time": datetime.datetime.strftime(data[8], DATETIME_FORMAT)
            if data[8] is not None
            else data[8],
            "end_time": datetime.datetime.strftime(data[9], DATETIME_FORMAT)
            if data[9] is not None
            else data[9],
            "close_time": datetime.datetime.strftime(data[10], DATETIME_FORMAT)
            if data[10] is not None
            else data[10],
        }
        for data in db.query(
            Post.ID,
            Post.Account_id,
            Post.Type,
            Post.Title,
            Post.Content,
            Post.Location,
            Post.Limit_member,
            Post.Create_time,
            Post.Start_time,
            Post.End_time,
            Post.Close_time,
        )
        .filter(
            Post.Close_time >= datetime.datetime.now(),
            Post.Close_time >= time,
            Post.ID != id,
        )
>>>>>>> Stashed changes
        .order_by(Post.Close_time.asc())
        .limit(5)
        .all()
    ]

<<<<<<< Updated upstream
    return event_info
=======
    if event_info:
        return event_info
    else:
        return []


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


async def delete_member_event_join(
    DeleteMemberEventJoinRequest: schema.DeleteMemberEventJoinRequest, db: Session
):
    db.query(PostParticipant).filter(
        PostParticipant.Account_id == DeleteMemberEventJoinRequest.member_id,
        PostParticipant.Post_id == DeleteMemberEventJoinRequest.event_id,
    ).delete()
    db.commit()


async def poster_cancel_post(CancelPostRequest: schema.CancelPostRequest, db: Session):
    db.query(Post).filter(
        Post.ID == CancelPostRequest.event_id,
    ).update({"Close_time": datetime.datetime.now()})
    db.commit()


async def get_member_event(member_id: str, db: Session):
    event_info = [
        {
            "ID": data[0],
            "poster_id": data[1],
            "type": data[2],
            "title": data[3],
            "content": data[4],
            "location": data[5],
            "limit_member": data[6],
            "create_time": datetime.datetime.strftime(data[7], DATETIME_FORMAT)
            if data[7] is not None
            else data[7],
            "start_time": datetime.datetime.strftime(data[8], DATETIME_FORMAT)
            if data[8] is not None
            else data[8],
            "end_time": datetime.datetime.strftime(data[9], DATETIME_FORMAT)
            if data[9] is not None
            else data[9],
            "close_time": datetime.datetime.strftime(data[10], DATETIME_FORMAT)
            if data[10] is not None
            else data[10],
        }
        for data in db.query(
            Post.ID,
            Post.Account_id,
            Post.Type,
            Post.Title,
            Post.Content,
            Post.Location,
            Post.Limit_member,
            Post.Create_time,
            Post.Start_time,
            Post.End_time,
            Post.Close_time,
        )
        .filter(Post.Account_id == member_id)
        .order_by(Post.Create_time.desc())
        .all()
    ]

    return event_info


async def get_post_participant_by_event_id(event_id: str, db: Session):
    post_participant = [
        {
            "account_id": data[0],
            "name": data[1],
            "email": data[2],
            "gender": data[3],
        }
        for data in db.query(
            PostParticipant.Account_id, Account.Name, Account.Email, Account.Gender
        )
        .join(Account, PostParticipant.Account_id == Account.ID)
        .filter(PostParticipant.Post_id == event_id)
        .all()
    ]

    return post_participant


async def update_event(postRequest: schema.UpdateEventRequest, db: Session):
    db.query(Post).filter(
        Post.ID == postRequest.event_id, Post.Account_id == postRequest.acount_id
    ).update(
        {
            "Title": postRequest.title,
            "Start_time": postRequest.start_time,
            "End_time": postRequest.end_time,
            "Content": postRequest.content,
            "Location": postRequest.location,
            "Limit_member": postRequest.member_num,
        }
    )
    db.commit()
>>>>>>> Stashed changes

from utils.db_model import Account
from sqlalchemy.orm.session import Session
from services.member import schema
import datetime


async def get_account_info_by_email(email: str, db: Session):

    account_info = [
        {
            "ID": data[0],
            "Name": data[1],
            "Email": data[2],
            "Gender": data[3],
            "Pwd": data[4]
        }
        for data in db.query(
            Account.ID,
            Account.Name,
            Account.Email,
            Account.Gender,
            Account.Password
        )
        .filter(
            Account.Email == email)
        .all()
    ]

    if len(account_info) > 0:
        return account_info[0]
    else:
        return None


async def get_account_info_by_id(account_id: str, db: Session):

    account_info = [
        {
            "ID": data[0],
            "Name": data[1],
            "Email": data[2],
            "Gender": data[3],
            "Pwd": data[4]
        }
        for data in db.query(
            Account.ID,
            Account.Name,
            Account.Email,
            Account.Gender,
            Account.Password
        )
        .filter(
            Account.ID == account_id)
        .all()
    ]

    if len(account_info) > 0:
        return account_info[0]
    else:
        return None


async def update_last_login_time(email: str, db: Session):

    db.query(Account).filter(Account.Email == email).update(
        {"Last_login_time": datetime.datetime.now()})
    db.commit()


async def create_member(uuid_code, hash_pwd, postRequest: schema.CreateMemberRequest, db: Session):

    db.add(
        Account(
            ID=uuid_code,
            Name=postRequest.name,
            Email=postRequest.email,
            Password=hash_pwd,
            Gender=postRequest.gender,
            Create_time=datetime.datetime.now(),
        )
    )
    db.commit()


async def edit_member_info(hash_pwd, editMemberInfoRequest: schema.EditMemberInfoRequest, db: Session):

    db.query(Account).filter(Account.ID == editMemberInfoRequest.account_id).update(
        {"Name": editMemberInfoRequest.name,
         "Gender": editMemberInfoRequest.gender,
         "Password": hash_pwd})
    db.commit()

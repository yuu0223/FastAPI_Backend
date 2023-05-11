from services.member import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response
from utils.basic import sha_256


async def login(loginRequest: schema.LoginRequest, db: Session):

    # 查詢是否有此email的會員資料
    account_info = await crud.get_account_info_by_email(loginRequest.email, db)
    hash_pwd = sha_256(loginRequest.pwd)

    if account_info:
        if hash_pwd != account_info["Pwd"]:
            return Response.Error(msg="密碼錯誤，請重新輸入")

        else:
            account_info_return = {
                "ID": account_info["ID"],
                "Name": account_info["Name"],
                "Email": account_info["Email"],
                "Gender": account_info["Gender"]}

            await crud.update_last_login_time(loginRequest.email, db)
            return Response.Success(data=account_info_return)
    else:
        return Response.Error(msg="查無此信箱")


async def create_member(uuid_code, createMemberRequest: schema.CreateMemberRequest, db: Session):

    account_info = await crud.get_account_info_by_email(createMemberRequest.email, db)

    if not account_info:
        hash_pwd = sha_256(createMemberRequest.pwd)
        await crud.create_member(uuid_code, hash_pwd, createMemberRequest, db)
        return Response.Success(data=None)
    else:
        return Response.Error(msg="此信箱已註冊過，請直接登入，謝謝")


async def edit_member_info(editMemberInfoRequest: schema.EditMemberInfoRequest, db: Session):

    account_info = await crud.get_account_info_by_id(editMemberInfoRequest.account_id, db)
    hash_pwd = sha_256(editMemberInfoRequest.pwd)

    if account_info:
        await crud.edit_member_info(hash_pwd, editMemberInfoRequest, db)
        return Response.Success(data=None)
    else:
        return Response.Error(msg="查無此帳號")

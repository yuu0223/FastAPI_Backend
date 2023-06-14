from services.medical import crud
from sqlalchemy.orm.session import Session
from utils.response import Response


async def get_medical_data(medical_id: int, db: Session):
    medical_info = await crud.get_medical_list(medical_id, db)

    if medical_info != []:
        return Response.Success(data=medical_info)
    elif medical_id == 0 and medical_info == []:
        return Response.Error(msg="目前沒有任何醫療文章唷～敬請期待！")
    else:
        return Response.Error(msg="底下沒有更多文章囉～")

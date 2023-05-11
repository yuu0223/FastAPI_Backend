from services.weather import crud
from sqlalchemy.orm.session import Session
from utils.response import Response


# 寫死的版本
async def get_weather_data(time, db: Session):

    weather_info = await crud.get_weather_data(time, db)

    if weather_info:
        return Response.Success(data=weather_info)
    else:
        return Response.Error(msg="查無一小時內天氣資訊")

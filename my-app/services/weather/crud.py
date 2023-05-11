from utils.db_model import Weather
from sqlalchemy.orm.session import Session
import datetime


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


async def get_weather_data(time, db: Session):

    weather_info = [
        {
            "StartTime": datetime.datetime.strftime(data[0], DATETIME_FORMAT) if data[0] is not None else data[0],
            "Wx": data[1],
            "PoP3h": data[2],
            "Temperature": data[3]
        }
        for data in db.query(
            Weather.StartTime,
            Weather.Wx,
            Weather.PoP3h,
            Weather.Temperature
        )
        .filter(time > Weather.StartTime)
        .order_by(Weather.StartTime.desc())
        .limit(1)
        .all()
    ]

    if len(weather_info) > 0:
        return weather_info[0]
    else:
        return None

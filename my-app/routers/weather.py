from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.weather import business
import datetime

router = APIRouter(prefix="/weather", tags=["weather"])


# new version
@router.get("/get_weather", summary="取得當下時間天氣預報")
async def get_weather_data(db: Session = Depends(get_db)):

    time = datetime.datetime.now()
    return await business.get_weather_data(time, db)


# # 程式二：判斷前端目前時間是幾點，然後判斷在資料庫的哪個時間區段，回傳該區段的較小時間的天氣數據
# # 定義API端點，接受前端傳送的時間參數
# @app.get("/weather")
# async def get_weather_data(time: str = Query(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))):

#     # 建立MySQL資料庫連線
#     cnx = mysql.connector.connect(**db_config)

#     # 建立游標
#     cursor = cnx.cursor()

#     # 執行SQL查詢語句，找到最接近且小於等於前端傳送時間的天氣數據
#     query = "SELECT * FROM weather WHERE startTime <= %s ORDER BY startTime DESC LIMIT 1"
#     cursor.execute(query, (time,))

#     # 取得查詢結果
#     result = cursor.fetchone()

#     # 關閉游標和連線
#     cursor.close()
#     cnx.close()

#     # 如果有查詢結果，回傳該筆天氣數據；否則回傳空字典
#     if result:
#         return {
#             "startTime": result[1],
#             "Wx": result[2],
#             "PoP3h": result[3],
#             "Temperature": result[4]
#         }
#     else:
#         return {}

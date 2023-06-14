from datetime import datetime, timedelta
import requests
import mysql.connector

# 抓取天氣資料並存入 MySQL 數據庫
def fetch_and_store_weather():
    # 抓取天氣資料
    authorization = "CWB-E0CBEB14-87B4-49A9-A4CA-A3240E63E9F4"
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-061?Authorization=CWB-E0CBEB14-87B4-49A9-A4CA-A3240E63E9F4"
    res = requests.get(url, {"Authorization": authorization})
    resJson = res.json()

    locations = resJson['records']['locations'][0]['location']
    wen_location = [x for x in locations if x['locationName'] == '文山區'][0]
    elementNames = wen_location['weatherElement']
    WeatherDescription_elementName = [x for x in elementNames if x['elementName'] == 'WeatherDescription'][0]
    time_descs = WeatherDescription_elementName['time']
    result = []

    # 取得現在時間
    now = datetime.now()

    # 創建與 MySQL 數據庫的連接
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        port="3307",
        user="root",
        password="root1234",
        database="test"
    )

    # 創建游標對象
    mycursor = mydb.cursor()

    # 插入數據
    for time_desc in time_descs:
        # 取得該時間段的開始時間
        start_time = datetime.strptime(time_desc['startTime'], '%Y-%m-%d %H:%M:%S')
        # 判斷該時間段是否為當天
        if start_time.date() == now.date():
            desc = time_desc['elementValue'][0]['value']
            parts = desc.split("。")
            desc_list = [part.strip() for part in parts[:3]]
            res = {'startTime': time_desc['startTime'], 'desc': desc_list}
            result.append(res)

            # 檢查是否已經有相同的 startTime 資料
            count_sql = "SELECT COUNT(*) FROM weather WHERE startTime = %s"
            count_val = (res['startTime'],)
            mycursor.execute(count_sql, count_val)
            count = mycursor.fetchone()[0]

            if count > 0:
                # 如果已有相同的 startTime 資料，則更新為最新的數據
                update_sql = "UPDATE weather SET Wx = %s, PoP3h = %s, Temperature = %s WHERE startTime = %s"
                update_val = (res['desc'][0], res['desc'][1], res['desc'][2], res['startTime'])
                mycursor.execute(update_sql, update_val)
            else:
                # 如果沒有相同的 startTime 資料，則插入新的數據
                insert_sql = "INSERT INTO weather (startTime, Wx, PoP3h, Temperature) VALUES (%s, %s, %s, %s)"
                insert_val = (res['startTime'], res['desc'][0], res['desc'][1], res['desc'][2])
                mycursor.execute(insert_sql, insert_val)
            
            # 提交更改
            mydb.commit()

    # 關閉游標和數據庫連接
    mycursor.close()
    mydb.close()
            
    return result

fetch=fetch_and_store_weather()
print(fetch)

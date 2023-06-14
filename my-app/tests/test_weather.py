import pytest
import requests

def test_weather_correct():
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-061?Authorization=CWB-E0CBEB14-87B4-49A9-A4CA-A3240E63E9F4"

    # 執行 API 呼叫並取得回應
    response = fetch_weather_data(url)

    # 確認回應的狀態碼為 200 (表示成功)
    assert response.status_code == 200

    # 確認回應的 JSON 資料中包含了 'records'、'locations' 和 'location' 的項目
    assert 'records' in response.json()
    assert 'locations' in response.json()['records']
    assert 'location' in response.json()['records']['locations'][0]

    # 取得文山區的資料
    locations = response.json()['records']['locations'][0]['location']
    wen_location = [x for x in locations if x['locationName'] == '文山區'][0]

    # 確認回應的 JSON 資料中包含了 'weatherElement' 的項目
    assert 'weatherElement' in wen_location

    # 取得天氣描述的資料
    elementNames = wen_location['weatherElement']
    WeatherDescription_elementName = [x for x in elementNames if x['elementName'] == 'WeatherDescription'][0]

    # 確認回應的 JSON 資料中包含了 'time' 的項目
    assert 'time' in WeatherDescription_elementName

    # 取得時間描述的資料
    time_descs = WeatherDescription_elementName['time']

    # 確認時間描述資料不為空
    assert len(time_descs) > 0

def fetch_weather_data(url):
    response = requests.get(url)
    return response

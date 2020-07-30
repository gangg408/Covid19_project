import requests
from pprint import pprint
from datetime import date, timedelta
import json
import xmltodict

def get_city_data():
    url="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

    params ={
        'servicekey':'Bo6IL1w83pOXx91pK/bBHvf1A/TQReOU6MNqGd55s+/V9yN7oXiYMqicecP06Jxkd0XEoJXsL18HXeWwiseTxQ==',
        'pageNo':'1',
        'numOfRows':'30',
        'startCreateDt':'20200726',
        'endCreateDt':'20200727',
    }

    res = requests.get(url, params=params)
    dict_data = xmltodict.parse(res.text)

    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)
    pprint(dict_data)
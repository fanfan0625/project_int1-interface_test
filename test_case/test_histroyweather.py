#!/usr/bin/env python3.6.1  
# encoding: utf-8  
# @Time    : 2018/6/24 15:51  
# @Author  : fanfan 
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_histroyweather.py  
# @Software: PyCharm Community Edition

import requests
from config import config
import unittest
import ddt
from lib import get_data


@ddt.ddt
class testHistoryWeather(unittest.TestCase):
    def setUp(self):
        self.provice_url = config.host + "province"
        self.city_url = config.host + "citys"
        self.weather_url = config.host + "weather"
        self.key = config.appkey

    def tearDown(self):
        pass

    def test_1get_provincelist(self):
        param = "key=" + self.key
        res = requests.get(self.provice_url, param)
        jsonRes = res.json()
        print (jsonRes)
        self.assertIn(jsonRes.get("reason"), '查询成功')
        reason = jsonRes.get("reason")
        print(reason)
        if reason == u'查询成功':
            result = jsonRes.get("result")
            print(len(result))
            for i in range(len(result)):
                js = result[i]
                provinces = js.get("province")
                if provinces == '广东':
                    self.province_id = result[i].get("id")
                    print(self.province_id)

    def test_2get_citylist(self):
        payload = {'key': self.key, 'province_id': 6}
        r = requests.post(self.city_url, data=payload)
        jsonRes = r.json()
        print (jsonRes)
        self.assertIn(jsonRes.get("reason"), "查询成功")

    @ddt.data(*[{"city_id": 1132, "weather_date": "2017-07-15"},
              {"city_id": 1132, "weather_date": "2017-07-16"},
              {"city_id": 1132, "weather_date": "2017-07-17"},
              {"city_id": 1132, "weather_date": "2017-07-18"}])

    @ddt.data(*get_data.get_histroyweather_data(r'.\testdata\testdata'))
    def test_3get_historyweather(self, data):
        #city_id = data['city_id']
        #weather_date = data['weather_date']
        payload = {"key": self.key, "city_id": data['city_id'], "weather_date": data['weather_date']}
        res = requests.post(self.weather_url, data=payload)
        jsonRes = res.json()
        print (jsonRes)
        self.assertIn(jsonRes.get("reason"), "查询成功")

if __name__ == "__main__":
    unittest.main()

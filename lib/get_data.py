#!/usr/bin/env python3.6.1  
# encoding: utf-8  
# @Time    : 2018/6/24 17:59  
# @Author  : fanfan 
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : get_data.py  
# @Software: PyCharm Community Edition

def get_histroyweather_data(filename = r'.\testdata\testdata'):
    data4weather = []
    with open(filename, 'r') as f:
        datasuite = f.readlines()
        for data in datasuite:
            lst = data.strip().split('|')
            item = {"city_id": lst[0],"weather_date": lst[1]}
            data4weather.append(item)
    return data4weather


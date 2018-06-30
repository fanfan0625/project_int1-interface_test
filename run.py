#!/usr/bin/env python3.6.1  
# encoding: utf-8  
# @Time    : 2018/6/24 16:21  
# @Author  : fanfan 
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : run.py  
# @Software: PyCharm Community Edition

import unittest
from test_suites import ranzhi_suite
from test_suites import weather_suite
from lib.HTMLTestRunner import HTMLTestRunner
import time

if __name__ == "__main__":
    #suite = ranzhi_suite.get_suite()
    suite = weather_suite.get_suite()
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_name = "test_report_{}.html".format(current_time)
    with open('reports/{}'.format(report_name), 'wb') as report:
        runner = HTMLTestRunner(
            stream=report,
            title="test_HistoryWeather",
            description="测试历史天气"
        )
        runner.run(suite)

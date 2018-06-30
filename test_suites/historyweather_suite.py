#!/usr/bin/env python3.6.1  
# encoding: utf-8  
# @Time    : 2018/6/24 16:12  
# @Author  : fanfan 
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : historyweather_suite.py  
# @Software: PyCharm Community Edition

from test_case.test_histroyweather import testHistoryWeather
import unittest

def get_suite():
    suite = unittest.TestSuite()
    #loader = unittest.TestLoader()
    #testcases = loader.loadTestsFromTestCase(testHistoryWeather)
    suite.addTest(testHistoryWeather.test_1get_provincelist())
    suite.addTest(testHistoryWeather.test_2get_citylist())
    suite.addTest(testHistoryWeather.test_3get_historyweather())
    return suite

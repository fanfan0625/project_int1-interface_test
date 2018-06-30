#!/usr/bin/env python3.6.1  
# encoding: utf-8  
# @Time    : 2018/6/24 16:21  
# @Author  : fanfan 
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : run.py  
# @Software: PyCharm Community Edition

from test_suites import historyweather_suite
import unittest
from lib import HTMLTestRunner
import time

if __name__ == "__main":
    suite = historyweather_suite.get_suite()
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_name = "test_report_{}.html".format(now_time)
    with open ('reports/{}'.format(report_name), 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u"获取天气预报自动化测试")
        runner.run(suite)

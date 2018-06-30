#!/usr/bin/env python3.6.1  
# encoding: utf-8  
# @Time    : 2018/6/24 14:38  
# @Author  : fanfan 
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_ranzhi_login.py  
# @Software: PyCharm Community Edition

import requests
import hashlib #md5
import re #正则表达式
import unittest

class testRanzhilogin(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost/ranzhi/www/sys/user-login.html'
        self.username = 'admin'
        self.password = '1234'
        pass

    def tearDown(self):
        pass

    def test_ranzhi_login(self):
        #1.请求登录页
        res = requests.get(self.url)
        #2.通过正则表达式获取v.random的值
        pattern = "(?=v.random = \).*(?=;<)"

        #3.对password进行加密
        #4.构造请求参数
        #5.发送请求
        #6.发送结果

        pass

if __name__ == '__main__':
    unittest.main()

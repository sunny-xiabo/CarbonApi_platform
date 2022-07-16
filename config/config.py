"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : config.py
# @Date : 2022/7/15 10:16 下午
"""

# 目录相关配置
import os

currentPath = os.path.dirname((os.path.abspath(os.path.join(__file__, os.pardir))))  # 文件根目录
logPath = os.path.join(currentPath, 'logs/')  # 日志存储地址
configPath = os.path.join(currentPath, 'config/')  # 配置存储地址
csvPath = os.path.join(currentPath, 'data/')  # csv存储地址
testcasePath = os.path.join(currentPath, 'test_cases/')  # 测试用例存储地址
allurejsonPath = os.path.join(currentPath, 'json/')  # allure报告所需json数据存储地址


# print(testcasePath)
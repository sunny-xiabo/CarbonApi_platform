"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : run.py
# @Date : 2022/7/16 2:21 下午
"""

import pytest
from config import config

'''
1、执行main函数，进行pytest单元测试
2、执行allure，生成报告
    allure generate ./json -o ./reports --clean
3、启动allure服务
    allure open reports --host 127.0.0.1 --port 8800
    输入地址 查看报告

-s: 显示程序中的print / logging 输出
-V：丰富信息模式，输出更详细的用例执行信息
-q: 安静模式，不输出环境信息
-k: 关键字匹配，用and区分：匹配范围（文件名、类名、函数名）
'''

if __name__ == '__main__':
    pytest.main(['-v', '-s', config.testcasePath, '--alluredir='+config.allurejsonPath])
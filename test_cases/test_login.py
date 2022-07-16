"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : test_login.py
# @Date : 2022/7/16 10:29 下午
"""

import allure
import pytest
from utils.requestDataUtil import RequestDataUtil
from utils.requestUtil import RequestUtil
from config import config

# 获取网络请求工具对象
ru = RequestUtil()

# 获取请求数据对象
rdu = RequestDataUtil('login')
list = rdu.getRequestData()


# 参数化
@pytest.fixture(scope='function', params=list)
def getData(request):
    return request.param


@allure.feature('用户')
class TestLogin:
    @allure.story('登录接口')
    def test_login(self,getData):
        # 发送请求
        result = ru.doRequest(method=getData['method'], url=getData['url'], params=getData['params'],
                              data=getData['data'], json=getData['json'], headers=getData['headers'])

        # 断言
        ru.assertResult(result, getData['validate']['statusCode'], getData['validate']['errorCode'],
                        getData['validate']['msg'])

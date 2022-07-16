"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : test_second_level.py
# @Date : 2022/7/16 2:01 下午
"""
import allure
import pytest
from utils.requestDataUtil import RequestDataUtil
from utils.requestUtil import RequestUtil
from config import config

# 获取网络请求工具对象
ru = RequestUtil()

# 获取请求数据对象
rdu = RequestDataUtil('second_level')
list = rdu.getRequestData()


# 参数化
@pytest.fixture(scope='function', params=list)
def getData(request):
    return request.param


@allure.feature('商品信息')
class TestSecondLevel:

    @allure.story('二级分页接口')
    def test_secondlevel(self, getData):
        # 发送请求
        result = ru.doRequest(method=getData['method'], url=getData['url'], params=getData['params'],
                              data=getData['data'], json=getData['json'], headers=getData['headers'])

        # 断言
        ru.assertResult(result, getData['validate']['statusCode'], getData['validate']['errorCode'],
                        getData['validate']['msg'])

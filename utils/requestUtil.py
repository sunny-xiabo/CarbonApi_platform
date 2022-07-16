"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : requestUtil.py
# @Date : 2022/7/16 1:27 下午
"""
import allure
import requests
from utils.log import logger


class RequestUtil:
    '''
    网络请求工具类
    '''

    def __doGet(self, url, params=None, **kwargs):
        """
        私有化get请求
        :param url:
        :param params:
        :param kwargs:
        :return:
        """
        result = requests.get(url=url, params=params, **kwargs)

        logger.info('请求路径：' + str(result.request.url))
        logger.info('请求方式：' + str(result.request.method))
        logger.info('请求头：' + str(result.request.headers))
        logger.info('请求体：' + str(result.request.body))
        logger.info('响应状态码：' + str(result.status_code))
        logger.info('响应头：' + str(result.headers))
        logger.info('响应文本内容：' + str(result.text))

        return result

    def __doPost(self, url, data=None, json=None, **kwargs):
        """
        私有化post请求
        :param url:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """
        result = requests.post(url=url, data=data, json=json, **kwargs)

        logger.info('请求路径：' + str(result.request.url))
        logger.info('请求方式：' + str(result.request.method))
        logger.info('请求头：' + str(result.request.headers))
        logger.info('请求体：' + str(result.request.body))
        logger.info('响应状态码：' + str(result.status_code))
        logger.info('响应头：' + str(result.headers))
        logger.info('响应文本内容：' + str(result.text))

        return result

    def doRequest(self, method, url, params=None, data=None, json=None, **kwargs):
        """

        :param method:
        :param url:
        :param params:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """
        if method == "GET":
            return self.__doGet(url=url, params=params, **kwargs)
        elif method == "POST":
            return self.__doPost(url=url, data=data, json=json, **kwargs)
        else:
            logger.info('暂时不支持的请求方式：' + str(method))

    # 断言 根据实际接口返回数据进行改写，字段不一定是status和msg
    def assertResult(self, result, statusCode, errorCode, msg):
        """
        断言实际接口返回数据
        :param result:
        :param statusCode:
        :param errorCode:
        :param msg:
        :return:
        """
        with allure.step('发生请求'):
            allure.attach(str(result.url), '请求路径')
            allure.attach(str(result.request.method), '请求方式')
            allure.attach(str(result.request.headers), '请求头')
            allure.attach(str(result.request.body), '请求体')

        with allure.step('获取响应'):
            allure.attach(str(result.status_code), '响应状态码')
            allure.attach(str(result.headers), '响应头')
            allure.attach(str(result.text), '响应文本')

        with allure.step('断言'):
            allure.attach(str(statusCode), '预期响应状态码')
            allure.attach(str(errorCode), '预期返回错误码 status')
            allure.attach(msg, '预期返回错误信息msg')

            assert result.status_code == int(statusCode)
            assert result.json()['status'] == int(errorCode)
            assert result.json()['msg'] == msg

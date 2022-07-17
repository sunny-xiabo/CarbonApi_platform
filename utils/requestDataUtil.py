"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : requestDataUtil.py
# @Date : 2022/7/16 12:53 下午
"""

from config import config
from data.apiUrl import HOST_URL
from utils.log import logger
from utils.YamlUtil import YamlUtil
from utils.CsvUtil import CsvUtil


class RequestDataUtil:
    '''
    获取请求数据的工具类
    '''

    def __init__(self, fileName):
        self.yamlFile = config.configPath + fileName + '.yml'
        self.csvFile = config.csvPath + fileName + '.csv'

    def getRequestData(self):
        """
        获取请求数据
        :return:
        """
        # 获取yaml工具对象
        yu = YamlUtil(self.yamlFile)
        # 获取CSV工具对象
        cu = CsvUtil(self.csvFile)

        requestDataList = []  # 定义一个空列表

        # 遍历CSV列表数据， dict表示一行数据
        for dict in cu.getCsvData():
            yamlDict = yu.getYamlData()  # 一条请求数据
            # URL拼接
            yamlDict['url'] = HOST_URL + yamlDict['url']
            # 判断headers
            headers = yamlDict['headers']
            if headers != None:
                for key in headers.keys():
                    headers[key] = dict[key]
            # 判断params
            params = yamlDict['params']
            if params != None:
                for key in params.keys():
                    params[key] = dict[key]
            # 判断 data
            data = yamlDict['data']
            if data != None:
                for key in data.keys():
                    data[key] = dict[key]

            # 判断 json
            json = yamlDict['json']
            if json != None:
                for key in json.keys():
                    json[key] = dict[key]

            # 判断 validate
            validate = yamlDict['validate']
            if validate != None:
                for key in validate.keys():
                    validate[key] = dict[key]

            # 添加到列表
            requestDataList.append(yamlDict)

        logger.info('组装请求数据：' + str(requestDataList))
        return requestDataList

#
# if __name__ == '__main__':
#     rdu = RequestDataUtil('second_level')
#     rdu.getRequestData()

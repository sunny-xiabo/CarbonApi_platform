"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : CsvUtil.py
# @Date : 2022/7/16 12:25 下午
"""

import csv
from config import config
from utils.log import logger


class CsvUtil:
    '''
    csv封装类
    '''

    def __init__(self, file):
        self.file = file

    # 读取csv数据，返回字典格式，字典键为第一行
    def getCsvData(self):
        """
        获取csv数据
        :return:
        """
        file_csv = open(file=self.file, mode='r', encoding='utf-8-sig')
        read_csv = list(csv.reader(file_csv))  # 读取的数据
        dictList = []
        for i in range(1, len(read_csv)):  # 从第二行开始读取数据
            dict = {}  # 一条数据的字典
            data = read_csv[i]  # 一条csv数据
            keys = read_csv[0]  # key数据
            for j in range(len(keys)):
                dict[keys[j]] = data[j]  # 组装一条字典
            dictList.append(dict)  # 添加到列表

        logger.info('读取CSV格式化后内容：' + str(dictList))
        return dictList

# if __name__ == '__main__':
#     cu = CsvUtil(config.csvPath+'second_level.csv')
#     cu2 = CsvUtil(config.csvPath+'login.csv')
#     cu.getCsvData()
#     cu2.getCsvData()

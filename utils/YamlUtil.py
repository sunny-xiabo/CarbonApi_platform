"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : YamlUtil.py
# @Date : 2022/7/16 12:06 上午
"""

import yaml
from utils.log import logger
from config import config


class YamlUtil:
    '''
    读取yaml配置数据工具类
    '''
    def __init__(self, file):
        self.file = file

    def getYamlData(self):
        """
        读取yaml配置数据
        :return:
        """
        # 读取yaml配置数据
        file = open(file=self.file, mode='r', encoding='utf-8')
        # yaml.load()函数转成字典格式 stream 操作的文件对象 Loader制定加载器对象
        j = yaml.load(stream=file, Loader=yaml.FullLoader)
        # 打印读取日志
        logger.info('读取yaml配置内容：' + str(j))
        return j


# if __name__ == '__main__':
#     yu = YamlUtil(config.configPath + 'second_level.yml')
#     yu.getYamlData()


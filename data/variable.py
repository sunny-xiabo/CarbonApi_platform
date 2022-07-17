"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : variable.py
# @Date : 2022/7/17 4:35 下午
"""

from utils.log import logger

'''
    全局变量  存储  获取
'''


class Variable:

    def set(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        # 保存一个键值对
        logger.info('保存键值对：key=' + str(key) + ', value=' + str(value))
        setattr(self, key, value)

    def get(self, key):
        """
        通过key 键获取值
        :param key:
        :return:
        """
        logger.info('获取键值对：key=' + str(key))
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return None


# 初始化对象供外面存取数据
var = Variable()

# if __name__ == '__main__':
#     var.set('name', 'zhangsan')
#     print(var.get('name'))

"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : log.py
# @Date : 2022/7/15 9:35 下午
"""

import logging
from config import config
import os

# 设置日志打印模块
class Logger(logging.Logger):
    '''
    日志封装工具类
    '''
    # 初始化函数 cmd_level控制台打印时日志默认级别, file_level写入日志文件默认级别
    def __init__(self, name='Dash', cmd_level=logging.DEBUG, file_level=logging.DEBUG):
        # 调用父类初始化函数
        super().__init__(name)
        try:
            self.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
            # 日志输出格式化
            logs_format = logging.Formatter(
                '[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] %(message)s')
            # 日志文件路径及名称
            self.log_file = os.path.join(config.logPath + '/runlog.txt')

            # 设置控制台输出
            terminal = logging.StreamHandler()
            terminal.setFormatter(logs_format)  # 设置控制台输出格式
            terminal.setLevel(cmd_level)  # 设置控制台输出的默认级别
            # 设置文件输出
            file_output = logging.FileHandler(self.log_file, 'a', encoding='utf-8')
            file_output.setFormatter(logs_format)  # 设置文件输出格式
            file_output.setLevel(file_level)  # 设置文件输出的默认级别
            # 添加日志输出方式
            self.addHandler(terminal)
            self.addHandler(file_output)
        except Exception as e:
            raise e


# 初始化 logger 对象 供外面使用
logger = Logger()

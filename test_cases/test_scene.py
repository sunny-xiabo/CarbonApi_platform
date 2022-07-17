"""
# -*- coding:utf-8 -*-
# @Author: bo xia
# @File : test_scene.py
# @Date : 2022/7/17 8:48 下午
"""
from utils.SceneRequestUtil import SceneRequestUtil
from utils.requestUtil import RequestUtil
import allure


@allure.feature('场景')
class TestScene:
    @allure.story('场景测试01')
    def test_scene_01(self):
        ru = RequestUtil()
        cjru = SceneRequestUtil('scene_01', ru)
        cjru.yamlAndRequest()

    @allure.story('场景测试02')
    def test_scene_02(self):
        ru = RequestUtil()
        cjru = SceneRequestUtil('scene_02', ru)
        cjru.yamlAndRequest()

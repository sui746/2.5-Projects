# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
functions = Element('search')
from common.readconfig import ReadConfig
import yaml
import pytest
import allure



class FunctionPage(WebPage,ReadConfig):
    """功能流程"""
    def login(self):
        """登录"""
        # url = ReadConfig.read_inifile(self,head="HOST",hand="HOST")
        url = ReadConfig.read_inifile(self,hand='HOST',head='HOST')
        WebPage.get_url(self,url)
        self.input_text(functions['账号'],'suihaonan')
        sleep()
        self.input_text(functions['密码'],'Abc123456')
        sleep()
        self.input_text(functions['验证码'],'FUCK')
        sleep()
        self.is_click(functions['登录按钮'])
        sleep()
        return self





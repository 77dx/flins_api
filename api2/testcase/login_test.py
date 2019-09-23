# -*- coding:utf-8 -*-
import allure
import pytest
from Conf.Config import Config
from Parameters.params import Login
import requests

class TestLogin:

    @allure.feature('Boss')
    @allure.severity('normal')
    @allure.story('Login')
    def test_basic_01(self):
        param = Login()
        url = param.url




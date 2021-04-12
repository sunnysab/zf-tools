# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 16:10
# @Author  : sunnysab
# @File    : base.py

import requests
from ..user import User
from ..environment import Environment


class BaseSession:
    """ Base session class """

    _user: str = None
    _passwd: str = None
    _session = requests.Session()
    _login_flag = False

    def __init__(self, username=None, password=None):
        self._user = username
        self._passwd = password

    def login(self) -> str:
        pass

    def is_login(self) -> bool:
        return self._login_flag

    def user(self) -> User:
        if not self._login_flag:
            raise Exception('You should login first.')

        return User(self._user, self._session)

    def environment(self) -> Environment:
        if not self._login_flag:
            raise Exception('You should login first.')

        return Environment(self._session)

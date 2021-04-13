# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 16:07
# @Author  : sunnysab
# @File    : sso.py
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 14:45
# @Author  : sunnysab
# @File    : auth.py

from lxml import etree

from ..global_config import URL
from .aes import *
from .base import BaseSession

_LOGIN_URL = 'https://authserver.sit.edu.cn/authserver/login'

_DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/82.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
}


class SsoSession(BaseSession):
    """ Adapter for SSO authorization of authserver.sit.edu.cn """

    def __init__(self, user: str, passwd: str):
        super().__init__(user, passwd)

    @staticmethod
    def _hash_password(salt: str, password: str) -> str:
        iv = rds(16)
        encrypt = Encrypt(key=salt, iv=iv)
        hashed_passwd = encrypt.aes_encrypt(rds(64) + password)
        return hashed_passwd

    def _get_login_page(self):
        response = self._session.get(_LOGIN_URL, headers=_DEFAULT_HEADERS, timeout=30)
        response.raise_for_status()

        page = etree.HTML(response.text)
        return page

    def _get_login_parameters(self, page, user: str, passwd: str):
        # Query basic parameters from page.
        form_fields = [
            ('lt', "//input[@name='lt']/@value"),
            ('dllt', "//input[@name='dllt']/@value"),
            ('execution', "//input[@name='execution']/@value"),
            ('_eventId', "//input[@name='_eventId']/@value"),
            ('rmShown', "//input[@name='rmShown']/@value"),
        ]

        result = dict()
        salt = str(page.xpath("//input[@id='pwdDefaultEncryptSalt']/@value")[0])
        for field, xpath_string in form_fields:
            result[field] = str(page.xpath(xpath_string)[0])

        result['username'] = user
        result['password'] = self._hash_password(salt, passwd)  # Encrypt password
        return result

    def _post_login_request(self, form: dict):
        response = self._session.post(_LOGIN_URL, data=form, headers=_DEFAULT_HEADERS, timeout=30,
                                      allow_redirects=False)
        if response.status_code == 302:  # Login successfully
            return 'OK'
        elif response.status_code == 200:  # Login failed
            error_page = etree.HTML(response.text)
            error_msg = error_page.xpath("//span[@id='msg']/text()")[0]
            return str(error_msg)

        response.raise_for_status()

    def login(self) -> str:
        redirect: str = URL.HOME + '/sso/jziotlogin'

        page = self._get_login_page()
        form = self._get_login_parameters(page, self._user, self._passwd)
        result = self._post_login_request(form)

        if result != 'OK':
            self._session.close()
            return result

        self._login_flag = True
        r = self._session.get(_LOGIN_URL + '?service=' + redirect, headers=_DEFAULT_HEADERS, timeout=30)
        r.raise_for_status()
        return 'success'

# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 16:08
# @Author  : sunnysab
# @File    : aes.py
# 摘自知乎专栏
# 原文：https://zhuanlan.zhihu.com/p/184968023
# 本文件摘自
# https://github.com/sunnysab/kite-string/


import base64
from math import floor
from random import random

from Crypto.Cipher import AES


def rds(num: int) -> str:
    chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
    retstr = ''
    for i in range(0, num):
        retstr += chars[floor(random() * len(chars))]
    return retstr


class Encrypt:
    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')

    # @staticmethod
    def pkcs7padding(self, text):
        """
        明文使用PKCS7填充
        """
        bs = 16
        length = len(text)
        bytes_length = len(text.encode('utf-8'))
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = chr(padding) * padding
        self.coding = chr(padding)
        return text + padding_text

    def aes_encrypt(self, content):
        """
        AES加密
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 处理明文
        content_padding = self.pkcs7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        # 重新编码
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def aes_decrypt(self, content):
        """
        AES解密
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        content = base64.b64decode(content)
        text = cipher.decrypt(content).decode('utf-8')
        return text.rstrip(self.coding)

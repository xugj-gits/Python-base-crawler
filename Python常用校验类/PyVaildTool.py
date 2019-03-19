#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   PyVaildTool.py
@Time    :   2019/03/19 17:24:09
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''
import re


class PyVaildTool(object):

    # 校验手机号
    @staticmethod
    def vaildPhoneNum(phoneNum):
        phone_pattern = re.compile(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
        if phone_pattern.match(phoneNum):
            return True
        else:
            return False


    # 校验邮箱有效性
    @staticmethod
    def vaildEmail(email):
        email_pattern = re.compile(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$')
        if email_pattern.match(email):
            return True
        else:
            return False


    # 校验身份证
    @staticmethod
    def vaildIDCard(idCard):
        idCard_pattern = re.compile(r'^\d{15}|\d{18}$')
        if idCard_pattern.match(idCard):
            return True
        else:
            return False

    
    # 校验密码 6-16位字母、数字）
    @staticmethod
    def vaildPwd(password):
        pwd_pattern = re.compile(r'^[0-9A-Za-z]{6,16}$')
        if pwd_pattern.match(password):
            return True
        else:
            return False

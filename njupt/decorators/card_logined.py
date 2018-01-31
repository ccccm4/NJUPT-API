# encoding: utf-8

"""
用户认证装饰器(判断一卡通是否已经登录)
"""
from njupt.error import CardNotLogin


def card_logined(func):
    def wrapper(self, *args, **kwargs):
        if self.verify:  # 利用状态量进行状态的判定
            return func(self, *args, **kwargs)
        else:
            raise CardNotLogin

    return wrapper

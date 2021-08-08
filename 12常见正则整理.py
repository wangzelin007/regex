# 1. 六位密码，不能出现连续两个数字
import re


def six_pass():
    re.match(r'^((?!\d\d)\w){6}$', '11abcd')
    re.match(r'^((?!\d\d)\w){6}$', '1a2b3c')
    # <re.Match object; span=(0, 6), match='1a2b3c'>
    re.match(r'^(\w(?!\d\d)){6}$', '11abcd')  # 错误示范
    # <re.Match object; span=(0, 6), match='11abcd'>


def digit():
    reg = r'\d'
    reg = r'[0-9]'
    reg = r'\d+'
    reg = r'[0-9]+'
    reg = r'\d{n}'
    reg = r'\d{n,}'
    reg = r'\d{m,n}'


def number():
    # 匹配正数、负数、小数
    reg = r'[-+]?\d+(?:\.\d+)?'
    # 非负整数
    reg = r'[1-9]\d*|0'
    # 非正整数
    reg = r'-[1-9]\d*|0'


def match_float():
    # 浮点数
    reg = r'-?\d+(?:\.\d+)?|\+?(?:\d+(?:\.\d+)?|\.\d+)'
    # 负浮点数
    reg = r'-\d+(?:\.\d+)?'
    # 正浮点数
    reg = r'\+?(?:\d+(?:\.\d+)?|\.\d+)'


def hexadecimal_number():
    reg = r'[0-9A-Fa-f]+'


def phone_number():
    reg = r'1(?:3\d|4[5-9]|5[0-35-9]|6[2567]|7[0-8]|8\d|9[1389])\d{8}'


def id_card():
    reg = r'[1-9]\d{14}(\d\d[0-9Xx])?'


def zip_code():
    # 添加断言，排除手机号、身份证号一部分的情况
    reg = r'(?<!\d)\d{6}(?!\d)'


def qq():
    reg = r'[1-9][0-9]{4,9}'


def chinese_characters():
    reg = re.compile(r'[\u4E00-\u9FFF]')
    reg.findall("学习正则regex")
    # ['学', '习', '正', '则']


def ipv4():
    pass


def ipv6():
    pass


def time():
    pass


def email_address():
    pass


def title():
    pass

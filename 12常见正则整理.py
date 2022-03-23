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
    # 由于 NFA 优先匹配最左侧，所以优先写最长的分支 3 位的情况
    reg = r'(?:1\d\d|2[0-4]\d|25[0-5]|0?[1-9]\d|0{0,2}\d)(?:\.(?:1\d\d|2[0-4]\d|25[0-5]|0?[1-9]\d|0{0,2}\d)){3}'


def ipv6():
    # ABCD:EF01:2345:6789:ABCD:EF01:2345:6789
    # 2001:0DB8:0000:0023:0008:0800:200C:417A
    # 2001:DB8:0:23:8:800:200C:417A
    # 前导
    reg = r'[0-9a-fA-F]{4}(?:\:(?:[0-9a-fA-F]{4})){7}'
    # 省略前导 0
    reg = r'(?:0|[1-9a-fA-F][0-9a-fA-F]{0,3})(?:\:(?:0|[1-9a-fA-F][0-9a-fA-F]{0,3})){7}'
    # 全匹配
    reg = r'(?:[0-9a-fA-F]{0,4})(?:\:(?:[0-9a-fA-F]{0,4})){7}'


def time():
    # yyyy-mm-dd
    reg = r'\d{4}-(?:1[0-2]|0?[1-9])-(?:[12]\d|3[01]|0?[1-9])'
    # 24 小时制 00:00 - 23:59
    reg = r'(?:2[0-3]|1\d|0?\d):(?:[1-5]\d|0?\d)'
    # 12 小时制 00:00 - 11:59
    reg = r'(?:1[01]|0?\d):(?:[1-5]\d|0?\d)'


def email_address():
    reg = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'


def title():
    reg = r'(?i)<title>.*?</title>'
    # 提取引号内容 [^"]+
    # 提取方括号内容 [^>]+

def brackets():
    string = '[Component Name 1] BREAKING] CHANGE: `az command a`: Make some customer-facing breaking change\r\n'
    reg1 = r'[\[](.*?)[\]]'
    # 最小匹配 Component Name 1
    reg2 = r'[\[](.*)[\]]'
    # 贪婪匹配 Component Name 1] BREAKING
    if re.findall(reg1, string):
        print(re.findall(reg1, string)[0])
    string = '[Component Name 1] [BREAKING] CHANGE: `az command a`: Make some customer-facing breaking change\r\n'
    if re.findall(reg1, string):
        print(re.findall(reg1, string)[0])
    string = 'Component Name 1 BREAKING CHANGE: `az command a`: Make some customer-facing breaking change\r\n'
    if re.findall(reg1, string):
        print(re.findall(reg1, string)[0])

if __name__ == '__main__':
    brackets()
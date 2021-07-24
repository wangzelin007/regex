import re
import regex
from pprint import pprint

def test1():
    test_string = '123456789012345\n' \
                  '123456789012345678'
    print(re.findall(r'(\d{15}(\d{3})?)', test_string))

def test2():
    test_string = ('2020-05-10 20:23:05'
                   '2021-07-24 23:40:00')
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})"
    matches = re.finditer(pattern, test_string)
    for match_num, match in enumerate(matches):
        print(f"{match.group()}")
    # groups    12       3       4        56       7       8
    pattern = r"((\d{4})-(\d{2})-(\d{2})) ((\d{2}):(\d{2}):(\d{2}))"
    matches = re.finditer(pattern, test_string)
    for match_num, match in enumerate(matches):
        print(f"{match.groups()}")

def test3():
    test_string = '123456789012345678'
    pattern1 = r"\d{15}(\d{3})?"
    # 不保存子组，子组不会被再次引用，提升性能，减少错误。
    pattern2 = r"\d{15}(?:\d{3})?"
    matches1 = re.finditer(pattern1, test_string)
    matches2 = re.finditer(pattern2, test_string)
    for match_num, match in enumerate(matches1):
        print(f"{match.group()}")
    for match_num, match in enumerate(matches2):
        print(f"{match.group()}")

def test4():
    test_string = "profile/wzl/"
    # 命名分组，相对数字分组更容易辨识，不易改变。
    pattern = r"^profile/(?P<username>\w+)/$"
    matches = re.finditer(pattern, test_string)
    for match_num, match in enumerate(matches):
        print(f"{match.group()}")

def test5():
    # 分组引用：查找 替换
    test_string = "the little cat cat is in the hat hat, we like it"
    pattern = r"(\w+) \1"
    # substitution
    subst = r"\1"
    result = re.sub(pattern, subst, test_string, 0, re.MULTILINE)
    if result:
        print(result)
    test_string = "2020-05-10 20:23:05"
    pattern = r"((\d{4})-(\d{2})-(\d{2})) ((\d{2}):(\d{2}):(\d{2}))"
    subst = r"日期\1 时间\5 \2年\3月\4日 \6时\7分\8秒"
    result = re.sub(pattern, subst, test_string, 0, re.MULTILINE)
    if result:
        print(result)

def test6():
    test_string = ("the little cat cat is in the hat hat hat, we like it.\n"
                   "the little   cat cat is in the hat hat hatt, we like it.")
    pattern = r"(\w+)(?:\s\1)+"
    # todo
    # pattern = r"(\b\w+)(?:\s+\1)+"
    # todo ??
    # pattern = r"/(\b\w+)(?:\s+\1)+/g"
    subst = r"\1"
    result = re.sub(pattern, subst, test_string, 0, re.MULTILINE)
    if result:
        print(result)


def test():
    test6()

if __name__ == '__main__':
    test()
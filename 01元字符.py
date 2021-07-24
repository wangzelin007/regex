import re
import regex
from pprint import pprint


def test1():
    test_string = "abcdefghijklmnopqrstuvwxyz" \
                  "0123456789" \
                  "~!@#$%^&*()_+{}[]:\";',.<>/?" \
                  "\n \r \t \f \v"  # 换行 回车 制表 换页 垂直制表
    # linux,unix :     \r\n
    # windows    :     \n
    # Mac OS     ：    \r

    # . 任意字符（换行除外）
    pprint(regex.findall(r".", test_string), compact=True)
    # \d 任意数字 digit
    pprint(regex.findall(r"\d", test_string), compact=True)
    # \D 任意非数字
    pprint(regex.findall(r"\D", test_string), compact=True)
    # \w 任意字母数字下划线 word
    pprint(regex.findall(r"\w", test_string), compact=True)
    # \W 任意非字母数字下划线
    pprint(regex.findall(r"\W", test_string), compact=True)
    # \s 任意空白符 space
    pprint(regex.findall(r"\s", test_string), compact=True)
    # \S 任意非空白符
    pprint(regex.findall(r"\S", test_string), compact=True)


def test2():
    test_string = "1234567890\n" \
                  "1\n" \
                  "123"
    # * 代表 0 到多次，多出来三次是因为匹配上了空白。
    # + 代表 1 到多次。
    pprint(regex.findall(r"\d*", test_string))
    pprint(regex.findall(r"\d+", test_string))


def test3():
    # https://zhuanlan.zhihu.com/p/43074437
    test_string = ("http://www.baidu.com\n"
                   "https://www.baidu.com\n"
                   "ftp://www.baidu.com/a.zip")
    pprint(regex.findall(r"((https?|ftp)://www.baidu.com)", test_string))


def test3_1():
    regex = r"(https?|ftp)://www.baidu.com"

    test_str = ("http://www.baidu.com\n"
                "https://www.baidu.com\n"
                "ftp://www.baidu.com/a.zip")
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        print(f"Match {matchNum} was found at {match.start()}-{match.end()}: {match.group()}")

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print(f"Group {groupNum} found at {match.start(groupNum)}-{match.end(groupNum)}: {match.group(groupNum)}")

def test4():
    # 手机号
    # 第 1 位固定为数字 1；
    # 第 2 位可能是 3 4 5 6 7 8 9；
    # 第 3 位 - 第 11 位 是 0 - 9 任意数字
    test_string = "13223232323" \
                  "12077876565" \
                  "+86-13223232323"
    pprint(regex.findall(r"((\+86-)?1[3-9]\d{9})", test_string))


def test():
    test4()


if __name__ == '__main__':
    test()

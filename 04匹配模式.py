import re
import regex

def test1():
    # 不区分大小写模式 case-insensitive (?i)
    test_string = "cat CAT Cat"
    pattern = r"(?i)cat" # i means case-insensitive
    print(re.findall(pattern, test_string))
    # same
    print(re.findall(r"cat", "cat CAT Cat", re.IGNORECASE))

    test_string = ("cat cat\n"
                   "CAT Cat\n"
                   "Cat cat\n"
                   "Cat Cat\n"
                   "CAT CAT")
    pattern = r"(?i)(cat) \1"
    subst = r"\1"
    results = re.sub(pattern, subst, test_string)
    if results:
        print(results)
    # todo 忽略大小写但是和前值完全一致
    pattern = r"((?i)cat) \1"
    print(regex.findall(pattern, test_string))

def test2():
    # 点号通配模式 Dot All (?s)
    pattern = r"(?s).+"
    test_string = ("cat cat\n"
                   "CAT Cat\n"
                   "Cat cat\n"
                   "Cat Cat\n"
                   "CAT CAT")
    print(re.findall(pattern, test_string))

def test3():
    # 多行匹配模式 Multiline (?m)
    # ^ 字符串的开头 $ 字符串的结尾
    # todo \A 字符串的开始 \Z 字符串的结尾
    pattern = r"^the|cat$"
    test_string = ("the little cat\n"
                   "the small cat")
    matches = re.finditer(pattern, test_string)
    for match_num, match in enumerate(matches):
        print(f"Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}")
    pattern = r"(?m)^the|cat$"
    matches = re.finditer(pattern, test_string)
    for match_num, match in enumerate(matches):
        print(f"Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}")

def test4():
    # 注释模式 Comment (?#comment)
    pattern = r"(\w+)(?#word) \1(?#word repeat again)"
    test_string = ("cat cat\n"
                   "CAT Cat\n"
                   "Cat cat\n"
                   "Cat Cat\n"
                   "CAT CAT")
    print(re.findall(pattern, test_string))

    pattern = r'''(?mx) # 使用多行模式和x模式，x模式下换行和空格都会被忽略
    ^           # 开头
    (\d{4})     # 年
    [ ]         # 空格
    (\d{2})     # 月
    $           # 结尾
    '''
    print(re.findall(pattern, '2020 06\n2020 07'))

def test5():
    test_string = ("<!DOCTYPE html>\n"
                   "<html>\n"
                   "<head>\n"
                   "    <title>学习正则</title>\n"
                   "</head>\n"
                   "<body>\n"
                   "</body>\n"
                   "</html>")
    pattern = r"(?si)<head>(.*)</head>"
    print(re.findall(pattern, test_string))

def test():
    test5()

if __name__ == '__main__':
    test()
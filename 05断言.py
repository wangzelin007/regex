# 断言指对匹配到的文本位置的限定
import re
import regex

def test1():
    # 单词边界 Word Boundary \b
    test_string = "tom asked me if I would go fishing with him tomorrow."
    print(re.sub(r"\btom\b", 'jerry', test_string))

def test2():
    # 行的开始和结束
    assert re.search("^\d{6}$", "1234567") is None
    assert re.search("^\d{6}$", "123456") is not None
    assert re.search("\A\d{6}\Z", "1234567") is None
    assert re.search("\A\d{6}\Z", "123456") is not None

def test3():
    # 环视 Look Around
    # (?<=Y) 左边是Y 肯定逆序环视 positive-lookbehind
    # (?<!Y) 左边不是Y 否定逆序环视 negative-lookbehind
    # (?=Y) 右边是Y 肯定顺序环视 positive-lookahead
    # (?!Y) 右边不是Y 否定顺序环视 negative-lookahead
    # 确定六位数邮编
    pattern = r"(?<!\d)\d{6}(?!\d)"
    test_string = ("130400\n"
                   "465441\n"
                   "4654000\n"
                   "138001380002")
    print(re.findall(pattern, test_string))
    # \b\w+\b == (?<!\w)\w+(?!\w) == (?<=\W)\w+(?=\W)
    # 注意环视不会被标记为子组

def test4():
    # 优化去重
    test_string = ("the little cat cat is in the hat hat, we like it.\n"
                   "the little cat cat2 is in the hat hat2, we like it.\n"
                   "the littel cat cat cat is in the hat, we like it.\n"
                   "the  the  the littel cat is in the hat, we like it.")
    pattern = r"\b(\w+)\b(\s+\b\1\b)+"
    subst = r"\1"
    result = re.sub(pattern, subst, test_string)
    if result:
        print(result)

def test():
    test4()

if __name__ == '__main__':
    test()
import re
import regex

def test1():
    test_string = "aaabb"
    assert re.findall(r'a+', 'aaabb') == ['aaa']
    assert re.findall(r'a*', test_string) == ['aaa', '', '', '']
    assert re.findall(r'a*?', test_string) == ['', 'a', '', 'a', '', 'a', '', '', '']

def test2():
    test_string = "\"the little cat\" is a toy, it looks \"a little bad\"."
    print(re.findall(r"\".+\"", test_string))
    print(re.findall(r"\".+?\"", test_string))

def test3():
    # 回溯有可能导致线上问题: cpu 跑满
    # 贪婪模式: 发生回溯
    assert regex.findall(r'xy{1,3}z', 'xyyz') == ['xyyz']
    # 非贪婪模式: 发生回溯
    assert regex.findall(r'xy{1,3}?z', 'xyyz') == ['xyyz']
    # 独占模式，类似贪婪匹配但不会发生回溯
    # 性能好，但是必须要确认好是否能满足需求
    assert regex.findall(r'xy{1,3}+z', 'xyyz') == ['xyyz']
    assert regex.findall(r'xy{1,2}+yz', 'xyyz') == []

def test4():
    # 提取所有单词 the little cat 看做一个单词
    test_string = "we found \"the little cat\" is in the hat, we like \"the little cat\""
    # 字母数字下划线 or 引号内非引号出现 1 到多次
    print(regex.findall(r'\w+|"[^"]+"', test_string))

def test():
    test4()

if __name__ == '__main__':
    test()


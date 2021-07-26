# 转义字符 Escape Character
import re

def test1():
    # 输入字符串 -字符串转义-> 字符/正则文字 -正则转义->正则表达式
    #   \\\\        ->          \\         ->        \
    # 使用 r 省略了第一步
    print(re.findall('\\\\|d', 'a*b+c?\\d123d\\'))
    print(re.findall(r'\\|d', 'a*b+c?\\d123d\\'))
    print(re.findall(r'[\\|d]', 'a*b+c?\\d123d\\'))
    # 元字符的转义
    print(re.findall(r'[\+|\*|\?]', '+*?'))
    # 括号的转义
    # [] {} 都只需要转义开括号
    # () 左右都需要转义
    print(re.findall('\(\)\[]\{}', '()[]{}'))
    print(re.findall('\(\)\[\]\{\}', '()[]{}'))

def test2():
    # 使用函数来消除特殊含义
    # Go regexp.QuoteMeta(text)
    # Java Pattern.quote(text)
    # PHP preg_quote(text)
    print(re.escape('\d'))
    print(re.findall(re.escape('\d'), '\d'))
    print(re.escape('[+]'))
    print(re.findall(re.escape('[+]'), '[+]'))

def test3():
    # 字符组需要转义的三种情况
    print("1. 脱字符在中括号中，且在第一个位置")
    print(re.findall(r'[^ab]', '^ab'))
    print(re.findall(r'[\^ab]', '^ab'))

    print("2. 中划线在中括号中，且不在首尾位置")
    print(re.findall(r'[a-c]', 'abc-'))
    print(re.findall(r'[a\-c]', 'abc-'))
    print(re.findall(r'[-ac]', 'abc-'))
    print(re.findall(r'[ac-]', 'abc-'))

    print("3. 右括号在中括号中，且不再首位")
    print(re.findall(r'[]ab]', ']ab'))
    # 代表 ab]
    print(re.findall(r'[a]b]', ']ab'))
    print(re.findall(r'[a]b]', 'ab]'))
    print(re.findall(r'[a\]b]', ']ab'))

    print("4. 字符组中的其他元字符")
    # 不具有特殊含义，仅代表本身
    print(re.findall(r'[.*+?()]', '[.*+?()]'))
    # 代表元字符
    print(re.findall(r'[\d]', 'd12\\'))

def test4():
    # regex is processed by two compilers：
    # programming language compiler and regexp compiler
    # 找到换行符 '\n' NL NL
    print(re.findall('\n', '\\n\n\\'))
    # 找到换行符 '\\n' '\'+'n' NL
    print(re.findall('\\n', '\\n\n\\'))
    # 找到换行符 '\\\n' '\'+NL NL
    print(re.findall('\\\n', '\\n\n\\'))
    # 找到反斜杠和字符n '\\\\n' '\'+'\'+'n' '\'+'n'
    print(re.findall('\\\\n', '\\n\n\\'))

def test():
    test4()

if __name__ == '__main__':
    test()
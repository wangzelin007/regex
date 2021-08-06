import re


# 1.search
def search():
    # \A\Z 确定边界是为了避免部分匹配： abc2020-06-01abc
    reg = re.compile(r'\A\d{4}-\d{2}-\d{2}\Z')  # compile 先编译可以提高效率
    assert reg.search('2020-06-01') is not None
    assert reg.match('2020-06-01') is not None  # 使用 match 时 \A 可以省略


# 2.提取文本内容
def find():
    # 没有子组时
    reg = re.compile(r'\d{4}-\d{2}')
    reg.findall('2020-05 2020-06')
    # ['2020-05', '2020-06']

    # 有子组时
    reg = re.compile(r'(\d{4})-(\d{2})')
    reg.findall('2020-05 2020-06')
    # [('2020', '05'), ('2020', '06')]

    # 使用 finditer 节约内存
    reg = re.compile(r'(\d{4})-(\d{2})')
    for match in reg.finditer('2020-05 2020-06'):
        print('date: ', match[0])  # match all
        print('year: ', match[1])  # match subgroup 1
        print('month: ', match[2])  # match subgroup 2
    # date: 2020-05
    # year: 2020
    # month: 05
    # date: 2020-06
    # year: 2020
    # month: 06


# 替换
def substitution():
    reg = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
    reg.sub(r'\3年\1月\2日', '02-20-2020 05-21-2020')
    # '2020年02月20日 2020年05月21日'

    # use \g<number> in sub, 避免歧义
    reg.sub(r'\g<3>年\g<1>月\g<2>日', '02-20-2020 05-21-2020')

    # return 替换次数
    reg.subn(r'\3年\1月\2日', '02-20-2020 05-21-2020')
    # ('2020年02月20日 2020年05月21日', 2)


# split 切割
def sp():
    "a b c\n\nd\t\n \te".split()
    # ['a', 'b', 'c', 'd', 'e']
    reg = re.compile(r'\W+')  # 任意非数字字母下划线
    reg.split("apple, pear! orange; tea")
    # ['apple'， 'pear'， 'orange'， 'tea']

    # limit split 次数，比如切一刀，变成两部分
    reg.split("apple, pear! orange; tea", 1)
    # ['apple', 'pear! orange; tea']

# coding:utf-8
"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
a = input("input a string:")
alpha = 0
space = 0
number = 0
other = 0
for i in a:
    if i.isalpha():
        alpha += 1
    elif i.isspace():
        space += 1
    elif i.isnumeric():
        number += 1
    else:
        other += 1
print("Letter = %s, Space = %s, Number = %s, Other = %s" % (alpha, space, number, other))

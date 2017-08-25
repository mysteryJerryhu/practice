# coding:utf-8
"""
题目：利用条件运算的嵌套来完成此题：
         学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""
score = int(input("Please input your grade:"))
if score >= 90:
    print("You got A!")
elif score >= 60:
    print("You got B!")
else:
    print("You got C!")

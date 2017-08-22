# coding:utf-8
"""
题目：输出 9*9 乘法口诀表。
m 控制行
n 控制列

into:
m=1
into----limit m+1=2
 n=1 p
----out

m=2
into----limit m+1=3
 n=1 p
 n=2 p
----out

m=3
into----limit m+1=4
 n=1 p
 n=2 p
 n=3 p
----out
....
...
"""
for m in range(1, 10):
    for n in range(1, m+1):
        print("%d*%d=%d" % (n, m, n*m), "", end='')
    print()

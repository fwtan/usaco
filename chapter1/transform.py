"""
ID: fuwen.t1
LANG: PYTHON3
TASK: transform
"""
from copy import deepcopy


def equal_indentity(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def rotate_90(a):
    b = deepcopy(a)
    n = len(b)
    for i in range(n):
        for j in range(n):
            b[i][j] = a[n-1-j][i]
    return b


def rotate_180(a):
    b = deepcopy(a)
    n = len(b)
    for i in range(n):
        for j in range(n):
            b[i][j] = a[n-1-i][n-1-j]
    return b


def rotate_270(a):
    b = deepcopy(a)
    n = len(b)
    for i in range(n):
        for j in range(n):
            b[i][j] = a[j][n-1-i]
    return b


def reflect1(a):
    b = deepcopy(a)
    n = len(b)
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][n-1-j]
    return b


def reflect2(a):
    b = deepcopy(a)
    n = len(b)
    for i in range(n):
        for j in range(n):
            b[i][j] = a[n-1-i][j]
    return b


fin  = open('transform.in', 'r')
fout = open('transform.out', 'w')
N = int(fin.readline().rstrip())

a, b = [], []
for i in range(N):
    row = [x for x in fin.readline().rstrip()]
    a.append(row)
for i in range(N):
    row = [x for x in fin.readline().rstrip()]
    b.append(row)

t = 7
if equal_indentity(b, rotate_90(a)):
    t = 1
elif equal_indentity(b, rotate_180(a)):
    t = 2
elif equal_indentity(b, rotate_270(a)):
    t = 3
elif equal_indentity(b, reflect1(a)):
    t = 4
else:
    d = reflect1(a)
    if equal_indentity(b, rotate_90(d)):
        t = 5
    elif equal_indentity(b, rotate_180(d)):
        t = 5
    elif equal_indentity(b, rotate_270(d)):
        t = 5
    elif equal_indentity(b, a):
        t = 6

fout.write('%d\n'%t)
fin.close()
fout.close()
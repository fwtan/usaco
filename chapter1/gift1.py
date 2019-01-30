"""
ID: fuwen.t1
LANG: PYTHON3
TASK: gift1
"""
from collections import OrderedDict
fin  = open('gift1.in', 'r')
fout = open('gift1.out', 'w')
N = int(fin.readline().rstrip())
account_table = OrderedDict()

for i in range(N):
    name = fin.readline().rstrip()
    account_table[name] = 0

current = 0
while current < N:
    name = fin.readline().rstrip()
    x, y = map(int, fin.readline().split())
    if y > 0:
        u = x % y
        v = x // y 
        account_table[name] += u - x 
        for i in range(y):
            name = fin.readline().rstrip()
            account_table[name] += v 
    current += 1

for name, val in account_table.items():
    fout.write('%s %d\n'%(name, val))

fin.close()
fout.close()
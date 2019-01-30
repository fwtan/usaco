"""
ID: fuwen.t1
LANG: PYTHON3
TASK: milk2
"""

fin  = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

N = int(fin.readline().rstrip())
range_list = []
for i in range(N):
    s, e = map(int, fin.readline().rstrip().split())
    range_list.append([s, e])
range_list = sorted(range_list, key=lambda x: x[0])
parent_list = list(range(0, N))
for i in range(1, N):
    curr = range_list[i]
    prev = range_list[i-1]
    if curr[0] <= prev[1]:
        parent_list[i] = parent_list[i-1]
        curr[1] = max(prev[1], curr[1])
r1 = 0
for i in range(N):
    p = parent_list[i]
    t = range_list[i][1] - range_list[p][0]
    r1 = max(r1, t)
r2 = 0
for i in range(1, N):
    p = parent_list[i]
    if p == i:
        t = range_list[i][0] - range_list[i-1][1]
        r2 = max(r2, t)

fout.write('%d %d\n'%(r1, r2))
fin.close()
fout.close()
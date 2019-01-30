"""
ID: fuwen.t1
LANG: PYTHON3
TASK: frac1
"""

import heapq
# s = time()

def get_children(n, m):
    children = []
    if (n+1) < m:
        children.append((n+1, m))
    if n < (m-1):
        children.append((n, m-1))
    return children


fin  = open('frac1.in', 'r')
fout = open('frac1.out', 'w')
N = int(fin.readline().rstrip())

indicator = [[True for i in range(N+1)] for j in range(N+1)]
out = [(0, 1)]
h = [(1/N, 1, N)]
heapq.heapify(h)
current_d = 0
while len(h) > 0:
    current_node = heapq.heappop(h)
    d, n, m = current_node
    children = get_children(n, m)
    if d > current_d:
        current_d = d
        out.append((n, m))
    num_children = len(children)
    for i in range(num_children):
        u, v = children[i]
        d = u/v
        if indicator[u][v]:
            heapq.heappush(h, (d, u, v))
            indicator[u][v] = False


if out[-1] != (1, 1):
    out.append((1, 1))
for i in range(len(out)):
    fout.write('%d/%d\n'%(out[i][0], out[i][1]))
fin.close()
fout.close()

# e = time()
# print(e-s)
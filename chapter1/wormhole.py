"""
ID: fuwen.t1
LANG: PYTHON3
TASK: wormhole
"""

def isCyclic(wg, xg):
    n = len(wg) 
    for i in range(n):
        p = i
        for j in range(n):
            p = wg[p]
            p = xg[p]
            if p < 0:
                break
        if p >= 0:
            return True
    return False


def helper(wg, xg):
    N = len(wg)
    i = 0

    while i < N:
        if wg[i] < 0:
            break
        i += 1
    
    if i == N:
        if isCyclic(wg, xg):
            return 1
        return 0

    count = 0
    for j in range(i+1, N):
        if wg[j] < 0:
            ng = [y for y in wg]
            ng[i] = j; ng[j] = i
            count += helper(ng, xg)
    return count
    

fin  = open('wormhole.in',  'r')
fout = open('wormhole.out', 'w')

N = int(fin.readline().rstrip())
locations = []
for i in range(N):
    locations.append([int(x) for x in fin.readline().rstrip().split()])

xg = [-1 for i in range(N)]
for i in range(N):
    for j in range(N):
        if locations[i][1] == locations[j][1] and locations[i][0] < locations[j][0]:
            if xg[i] < 0 or locations[j][0] < locations[xg[i]][0]:
                xg[i] = j


wg = [-1 for i in range(N)]
count = helper(wg, xg)

fout.write(str(count) + '\n')
fin.close()
fout.close()
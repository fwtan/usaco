"""
ID: fuwen.t1
LANG: PYTHON3
TASK: skidesign
"""

fin  = open('skidesign.in',  'r')
fout = open('skidesign.out', 'w')

N = int(fin.readline().rstrip())
H = []
for i in range(N):
    H.append(int(fin.readline().rstrip()))
H = sorted(H)
diff = max(H[-1] - H[0] - 17, 0)

min_cost = 1000000000
for x in range(diff):
    y = diff - x 
    cost = x**2 + y**2
    heights = [u for u in H]
    heights[0] += x
    heights[N-1] -= y
    # forward
    for i in range(1, N):
        d = heights[i-1] - heights[i]
        if d <= 0:
            break
        cost += d**2
        heights[i] += d
    # backward
    for i in range(N-2, -1, -1):
        d = heights[i] - heights[i+1]
        if d <= 0:
            break 
        cost += d**2
        heights[i] -= d
    if min_cost > cost:
        min_cost = cost

if min_cost == 1000000000:
    min_cost = 0
fout.write(str(min_cost) + '\n')
fin.close()
fout.close()







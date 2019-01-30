"""
ID: fuwen.t1
LANG: PYTHON3
TASK: ariprog
"""

fin  = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')

N = int(fin.readline().rstrip())
M = int(fin.readline().rstrip())

max_val = 2 * (M+1) * (M+1) 
valid_mask = [False] * max_val
for i in range(M+1):
    for j in range(M+1):
        valid_mask[i*i + j*j] = True

progressions = []
for a in range(max_val-N+2):
    if not valid_mask[a]:
        continue
    for b in range(1, int((max_val - a)/(N-1) + 0.5) + 1):
        if a + (N-1) * b > max_val:
            break
        flag = True
        for i in range(N):
            print(a, b, a + b * i)
            if not valid_mask[a + b * i]:
                flag = False
                break
        if flag:
            progressions.append((b, a))
        

if len(progressions) > 0:
    progressions = sorted(progressions)
    for i in range(len(progressions)):
        fout.write('%d %d\n'%(progressions[i][1], progressions[i][0]))
else:
    fout.write('NONE\n')

fin.close()
fout.close()
"""
ID: fuwen.t1
LANG: PYTHON3
TASK: numtri
"""

fin  = open('numtri.in', 'r')
fout = open('numtri.out', 'w')

N = int(fin.readline().rstrip())
T = []
S = []
for i in range(N):
    r1 = [int(x) for x in fin.readline().rstrip().split()]
    r2 = [0] * len(r1)
    T.append(r1)
    S.append(r2)

S[0][0] = T[0][0]
for i in range(N-1):
    for j in range(len(T[i])):
        S[i+1][j] = max(S[i][j] + T[i+1][j], S[i+1][j])
        S[i+1][j+1] = max(S[i][j] + T[i+1][j+1], S[i+1][j+1])

max_sum = 0
for x in S[-1]:
    max_sum = max(max_sum, x)

fout.write(str(max_sum) + '\n')
fin.close()
fout.close()
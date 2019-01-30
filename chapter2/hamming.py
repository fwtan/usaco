"""
ID: fuwen.t1
LANG: PYTHON3
TASK: hamming
"""

def hamming_distance(x, y):
    x = '{0:b}'.format(x^y)
    d = 0
    for i in x:
        if i == '1':
            d += 1
    return d

        
fin  = open('hamming.in', 'r')
fout = open('hamming.out', 'w')

N, B, D = list(map(int, fin.readline().rstrip().split()))

# N = 64
# B = 8
# D = 2

max_val = 2**B 
out = [0]
for i in range(1, max_val):
    if len(out) == N:
        break
    flag = True
    for j in range(len(out)):
        if hamming_distance(out[j], i) < D:
            flag = False
            break
    if flag:
        out.append(i)

while len(out) > 0:
    fout.write('%s\n'%(' '.join(map(str, out[:10]))))
    if len(out) > 10:
        out = out[10:]
    else:
        out = []

fin.close()
fout.close()
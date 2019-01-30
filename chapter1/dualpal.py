"""
ID: fuwen.t1
LANG: PYTHON3
TASK: dualpal
"""

fin  = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

N, S = map(int, fin.readline().rstrip().split())


def digit_str(n):
    if n < 10:
        return str(n)
    else:
        return chr(n-10 + ord('A'))


def toStr(n, base):
    if n < base:
        return digit_str(n)
    else:
        return toStr(n//base, base) + digit_str(n % base)


i = S+1
cands = []
while len(cands) < N:
    c = 0
    for B in range(2, 11):
        x = toStr(i, B)
        if x == x[::-1]:
            c += 1
        if c > 1:
            break
    if c > 1:
        cands.append(i)
    i += 1

for x in cands:
    fout.write('%d\n'%x)

fin.close()
fout.close()









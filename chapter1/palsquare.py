"""
ID: fuwen.t1
LANG: PYTHON3
TASK: palsquare
"""

fin  = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

B = int(fin.readline().rstrip())

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

for i in range(1, 301):
    x = i * i 
    # print(x)
    y = toStr(x, B)
    # print(y)
    if y == y[::-1]:
        fout.write('%s %s\n'%(toStr(i, B), y))

fin.close()
fout.close()
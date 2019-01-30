"""
ID: fuwen.t1
LANG: PYTHON3
TASK: test
"""
fin  = open('test.in', 'r')
fout = open('test.out', 'w')
x, y = map(int, fin.readline().split())
z    = x + y
fout.write(str(z) + '\n')
fin.close()
fout.close()
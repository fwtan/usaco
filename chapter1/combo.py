"""
ID: fuwen.t1
LANG: PYTHON3
TASK: combo
"""

fin  = open('combo.in', 'r')
fout = open('combo.out', 'w')

N = int(fin.readline().rstrip())
x, y, z = [int(x) for x in fin.readline().rstrip().split()]
u, v, w = [int(x) for x in fin.readline().rstrip().split()]

# x, u = max(x, u), min(x, u)
# y, v = max(y, v), min(y, v)
# z, w = max(z, w), min(z, w)

count = min(N, 5) ** 3 * 2
i = len(set([(x-2)%N, (x-1)%N, x%N, (x+1)%N, (x+2)%N]).intersection([(u-2)%N, (u-1)%N, u%N, (u+1)%N, (u+2)%N]))
j = len(set([(y-2)%N, (y-1)%N, y%N, (y+1)%N, (y+2)%N]).intersection([(v-2)%N, (v-1)%N, v%N, (v+1)%N, (v+2)%N]))
k = len(set([(z-2)%N, (z-1)%N, z%N, (z+1)%N, (z+2)%N]).intersection([(w-2)%N, (w-1)%N, w%N, (w+1)%N, (w+2)%N]))

count -= i * j * k
    
fout.write(str(count) + '\n')

fin.close()
fout.close()

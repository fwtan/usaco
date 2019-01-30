"""
ID: fuwen.t1
LANG: PYTHON3
TASK: sprime
"""

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0:
        return False
    i = 2
    while i * i <= x:
        if x%i == 0:
            return False 
        i += 1
    return True

def helper(x, level, N):
    if not is_prime(x):
        return []
    
    if level == N:
        return [x]
    
    l = []
    for i in range(1, 10):
        y = int(str(x) + str(i))
        l = l + helper(y, level+1, N)
    return l
        
fin  = open('sprime.in', 'r')
fout = open('sprime.out', 'w')

N = int(fin.readline().rstrip())

l = []
for i in range(2, 10):
    l += helper(i, 1, N)

for i in range(len(l)):
    fout.write(str(l[i]) + '\n')

fin.close()
fout.close()
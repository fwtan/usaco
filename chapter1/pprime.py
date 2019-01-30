"""
ID: fuwen.t1
LANG: PYTHON3
TASK: pprime
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


def helper(prefix, a, b, max_level):
    cur_level = len(prefix)
    cands = []
    if cur_level == 0:
        for i in range(1, 10):
            cands += helper(prefix+[i], a, b, max_level)
    elif cur_level < (max_level + max_level % 2) // 2:
        for i in range(0, 10):
            cands += helper(prefix+[i], a, b, max_level)
    else:
        prefix = ''.join(map(str, prefix))
        n = len(prefix)
        if n * 2 == max_level:
            p = int(prefix + prefix[::-1]) 
        else:
            p = int(prefix + prefix[::-1][1:])
        if p >= a and p <= b:
            cands = [p]
        else:
            cands = []
    return cands

        
def palindrome(a, b, num_digits):
    return helper([], a, b, num_digits)


fin  = open('pprime.in', 'r')
fout = open('pprime.out', 'w')

a, b = [int(x) for x in fin.readline().rstrip().split()]

cur_level = 1
while True:
    if int(''.join(['9']*cur_level)) > a:
        min_level = cur_level
        break
    cur_level += 1
cur_level = 1
while True:
    if 10**cur_level > b:
        max_level = cur_level
        break
    cur_level += 1

cands = []
for i in range(min_level, max_level+1):
    cands += palindrome(a, b, i)

l = []
for x in cands:
    if is_prime(x):
        l.append(x)

for i in range(len(l)):
    fout.write(str(l[i]) + '\n')

fin.close()
fout.close()
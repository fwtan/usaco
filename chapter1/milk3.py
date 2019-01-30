"""
ID: fuwen.t1
LANG: PYTHON3
TASK: milk3
"""

fin  = open('milk3.in', 'r')
fout = open('milk3.out', 'w')

A, B, C = [int(x) for x in fin.readline().rstrip().split()]

states = {(0,0,C):C}
q = [(0,0,C)]
while len(q) > 0:
    x, y, z = q[0]
    q = q[1:]

    if x > 0:
        if y < B:
            a = min(B-y, x)
            s = (x-a, y+a, z)
            if states.get(s, None) is None:
                states[s] = z
                q.append(s)
        if z < C:
            a = min(C-z, x)
            s = (x-a, y, z+a)
            if states.get(s, None) is None:
                states[s] = z+a
                q.append(s)
    if y > 0:
        if x < A:
            a = min(A-x, y)
            s = (x+a, y-a, z)
            if states.get(s, None) is None:
                states[s] = z
                q.append(s)
        if z < C:
            a = min(C-z, y)
            s = (x, y-a, z+a)
            if states.get(s, None) is None:
                states[s] = z+a
                q.append(s)
    if z > 0:
        if x < A:
            a = min(A-x, z)
            s = (x+a, y, z-a)
            if states.get(s, None) is None:
                states[s] = z-a
                q.append(s)
        if y < B:
            a = min(B-y, z)
            s = (x, y+a, z-a)
            if states.get(s, None) is None:
                states[s] = z-a
                q.append(s)

# print(len(states))

amounts = []
for k, v in states.items():
    if k[0] == 0:
        amounts.append(v)
amounts = sorted(list(set(amounts)))

    
fout.write(' '.join(map(str, amounts))+'\n')
fin.close()
fout.close()
"""
ID: fuwen.t1
LANG: PYTHON3
TASK: milk
"""

fin  = open('milk.in', 'r')
fout = open('milk.out', 'w')

N, M = [int(x) for x in fin.readline().rstrip().split()]

storage = []
for i in range(M):
    P, A = [int(x) for x in fin.readline().rstrip().split()]
    storage.append((P, A))
storage = sorted(storage, key=lambda x:x[0])
cost = 0
amount = 0
i = 0
while i < M:
    take_all = amount + storage[i][1]
    if take_all > N:
        break
    amount = take_all
    cost += storage[i][0] * storage[i][1]
    i += 1
if i < len(storage):
    cost += (N - amount) * storage[i][0]
fout.write(str(cost) + '\n')
fin.close()
fout.close()

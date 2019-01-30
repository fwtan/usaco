"""
ID: fuwen.t1
LANG: PYTHON3
TASK: sort3
"""

fin  = open('sort3.in', 'r')
fout = open('sort3.out', 'w')

N = int(fin.readline().rstrip())
counts = [0] * 4

digits = []
for i in range(N):
    d = int(fin.readline().rstrip())
    digits.append(d)
    counts[d] += 1

# print(counts)

range_counts = []
c1 = [0] * 4
for i in range(counts[1]):
    c1[digits[i]] += 1
range_counts.append(c1)
c2 = [0] * 4
for i in range(counts[1], counts[1]+counts[2]):
    c2[digits[i]] += 1
range_counts.append(c2)
c3 = [0] * 4
for i in range(counts[1]+counts[2], N):
    c3[digits[i]] += 1
range_counts.append(c3)

# print('-----')
# for x in range_counts:
#     print(x)

exchange = 0
e12 = min(range_counts[1][1], range_counts[0][2])
exchange += e12
range_counts[0][1] += e12
range_counts[1][2] += e12
range_counts[1][1] -= e12
range_counts[0][2] -= e12 

e13 = min(range_counts[2][1], range_counts[0][3])
exchange += e13
range_counts[0][1] += e13
range_counts[2][3] += e13
range_counts[2][1] -= e13
range_counts[0][3] -= e13 

e23 = min(range_counts[2][2], range_counts[1][3])
exchange += e23
range_counts[1][2] += e23
range_counts[2][3] += e23
range_counts[2][2] -= e23
range_counts[1][3] -= e23 

exchange += 2 * (range_counts[0][2] + range_counts[0][3])

# print('-----')

# for x in range_counts:
#     print(x)

# print(exchange)




# for i in range(counts[1]):
#     if digits[i] == 2:
#         for j in range()
#         exchange += 1
# for i in range(counts[1], counts[1]+counts[2]):
#     if digits[i] == 3:
#         exchange += 1

fout.write(str(exchange) + '\n')
fin.close()
fout.close()
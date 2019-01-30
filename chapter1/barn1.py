"""
ID: fuwen.t1
LANG: PYTHON3
TASK: barn1
"""

fin  = open('barn1.in', 'r')
fout = open('barn1.out', 'w')

M, S, C = [int(x) for x in fin.readline().rstrip().split()]
O = []
for i in range(C):
    ind = int(fin.readline().rstrip())
    O.append(ind)
O = sorted(O)

range_list = []
gap_list = []
sp, ep = 0, 0
for i in range(1, len(O)):
    if O[i] == O[ep]+1:
        ep = i 
    else:
        range_list.append((O[sp], O[ep]))
        gap_list.append(O[i] - O[ep])
        sp, ep = i, i
range_list.append((O[sp], O[ep]))
gap_list = zip(gap_list, range(len(gap_list)))
gap_inds = sorted(gap_list, key=lambda x:-x[0])
gap_inds = [x[1] for x in gap_inds]
gap_inds = sorted(gap_inds[:M-1])

out, gind, sp = 0, 0, 0
while gind < len(gap_inds):
    ep = gap_inds[gind]
    u = range_list[sp][0]
    v = range_list[ep][1]
    out += v - u + 1
    sp = gap_inds[gind]+1
    gind += 1

out += range_list[-1][1] - range_list[sp][0] + 1

fout.write(str(out) + '\n')


fin.close()
fout.close()

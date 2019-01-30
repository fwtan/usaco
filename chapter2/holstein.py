"""
ID: fuwen.t1
LANG: PYTHON3
TASK: holstein
"""

def subtract(baseline, v):
    return [baseline[i] - v[i] for i in range(len(v))]

def done(baseline):
    flag = True
    for i in range(len(baseline)):
        if baseline[i] > 0:
            flag = False 
            break
    return flag


fin  = open('holstein.in', 'r')
fout = open('holstein.out', 'w')

V = int(fin.readline().rstrip())
R = list(map(int, fin.readline().rstrip().split()))
G = int(fin.readline().rstrip())
vitamins = []
for i in range(G):
    vitamins.append(list(map(int, fin.readline().rstrip().split())))
    # print(vitamins[i])
chosen = [0] * G

def helper(start_ind, current_chosen, baseline):
    if done(baseline):
        n_types = 0
        for i in range(len(current_chosen)):
            if current_chosen[i] > 0:
                n_types += 1
        out = [n_types] + current_chosen
        return [out]
    all_outs = []
    for i in range(start_ind, len(current_chosen)):
        if current_chosen[i] == 0:
            next_chosen = [x for x in current_chosen]
            next_chosen[i] = 1
            next_baseline = subtract(baseline, vitamins[i])
            current_out = helper(i+1, next_chosen, next_baseline)
            if len(current_out) > 0:
                if len(all_outs) == 0 or all_outs[-1][0] > current_out[0][0]:
                    all_outs = current_out
                elif all_outs[-1][0] == current_out[0][0]:
                    all_outs = all_outs + current_out
    return all_outs

outs = helper(0, chosen, R)
# for x in outs:
#     print(x)
if len(outs) > 1:
    outs = sorted(outs, key=lambda x: x[1:], reverse=True)

final = outs[0]
types = []
for i in range(1, G+1):
    if final[i] > 0:
        types.append(i)
final = ' '.join(map(str, [final[0]] + types))
fout.write(final + '\n')
fin.close()
fout.close()
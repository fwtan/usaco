"""
ID: fuwen.t1
LANG: PYTHON3
TASK: crypt1
"""

def helper(digit_list):
    n = len(digit_list)
    digit_set = set(digit_list)

    count = 0
    for i in range(n):
        e = digit_list[i]
        for j in range(n):
            c = digit_list[j]
            if not (int(str(c * e)[-1]) in digit_set):
                continue
            for u in range(n):
                a = digit_list[u]
                if len(str(a * e)) > 1:
                    continue
                for v in range(n):
                    b = digit_list[v]
                    p1 = int(''.join(map(str, [a,b,c]))) * e
                    if len(str(p1)) > 3:
                        continue
                    tmp = str(p1)
                    flag = True
                    for x in tmp:
                        if not (int(x) in digit_set):
                            flag = False
                            break
                    if not flag:
                        continue
                    for w in range(n):
                        d = digit_list[w]
                        tmp = str(a * d)
                        if len(tmp) > 1:
                            continue
                        p2 = int(''.join(map(str, [a,b,c]))) * d
                        if len(str(p2)) > 3:
                            continue
                        tmp = str(p2)
                        flag = True
                        for x in tmp:
                            if not (int(x) in digit_set):
                                flag = False
                                break
                        if not flag:
                            continue
                        tmp = str(p1 + 10 * p2)
                        if len(tmp) > 4:
                            continue
                        flag = True
                        for x in tmp:
                            if not (int(x) in digit_set):
                                flag = False
                                break
                        if flag:
                            count += 1
                            # print(a, b, c, d, e, tmp)
    
    return count
                        
                     



fin  = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')

N = int(fin.readline().rstrip())
digit_list = [int(x) for x in fin.readline().rstrip().split()]
digit_list = sorted(digit_list)

count = helper(digit_list)

fout.write(str(count) + '\n')

fin.close()
fout.close()
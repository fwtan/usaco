"""
ID: fuwen.t1
LANG: PYTHON3
TASK: ride
"""
fin  = open('ride.in', 'r')
fout = open('ride.out', 'w')
comet_string = fin.readline().rstrip()
comet_number = [ord(x) - ord('A') + 1 for x in comet_string]
group_string = fin.readline().rstrip()
group_number = [ord(x) - ord('A') + 1 for x in group_string]

comet_product = 1
for x in comet_number:
    comet_product *= x

group_product = 1
for x in group_number:
    group_product *= x 

out = 'STAY'
if comet_product % 47 == group_product % 47:
    out = 'GO'

fout.write(str(out) + '\n')
fin.close()
fout.close()
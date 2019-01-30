"""
ID: fuwen.t1
LANG: PYTHON3
TASK: friday
"""

def next_date(prev_date, num_days_last_month):
    return (prev_date + num_days_last_month % 7) % 7

fin  = open('friday.in', 'r')
fout = open('friday.out', 'w')

N = int(fin.readline().rstrip())
counts = [0] * 7
start_year = 1900
end_year = 1900 + N
prev_date = 4 # Dec. 13, 1899 is a Wednesday
for y in range(start_year, end_year):
    for m in range(0, 12):
        if m in [0, 1, 3, 5, 7, 8, 10]: # when the previous (not current) month has 31 days
            prev_date = next_date(prev_date, 31)
        elif m == 2:
            if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
                prev_date = next_date(prev_date, 29)
            else:
                prev_date = next_date(prev_date, 28)
        else:
            prev_date = next_date(prev_date, 30)
        counts[prev_date] += 1 
fout.write('%d %d %d %d %d %d %d\n'%tuple(counts))
fin.close()
fout.close()
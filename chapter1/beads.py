"""
ID: fuwen.t1
LANG: PYTHON3
TASK: beads
"""

#################################################################
# My solution
#################################################################
# def helper(necklace, x, left_bead):
#     n = len(necklace)
#     right_bead = necklace[x]
#     count = 0
#     for offset in range(-1, -n+1, -1):
#         curr_index = (x + offset + n) % n
#         curr_bead = necklace[curr_index]
#         if curr_bead != 'w' and curr_bead != left_bead:
#             break
#         count += 1
#     end_t = curr_index
#     termination = False
#     for curr_index in range(x, n):
#         if x == 0 and curr_index >= end_t:
#             termination = True
#             break
#         curr_bead = necklace[curr_index]
#         if curr_bead != 'w' and curr_bead != right_bead:
#             break
#         count += 1
#         if curr_index == n-1:
#             termination = True
    
#     return count, curr_index, right_bead, termination


# fin  = open('beads.in', 'r')
# fout = open('beads.out', 'w')

# N = int(fin.readline().rstrip())
# necklace = fin.readline().rstrip()

# # compute the first turning point
# prev_bead = necklace[0]
# for first_t in range(N):
#     bead = necklace[first_t]
#     if prev_bead == 'w' or prev_bead == bead:
#         prev_bead = bead
#     else:
#         break
# necklace = necklace[first_t:] + necklace[:first_t]
# curr_index = 0
# max_num_beads = -1
# termination = False

# while not termination:
#     curr_num_beads, next_index, prev_bead, termination = helper(necklace, curr_index, prev_bead)
#     max_num_beads = max(max_num_beads, curr_num_beads)
#     curr_index = next_index

# fout.write(str(max_num_beads) + '\n')
# fout.close()

#################################################################
# DP solution
#################################################################

fin  = open('beads.in', 'r')
fout = open('beads.out', 'w')

N = int(fin.readline().rstrip())
necklace = fin.readline().rstrip()
necklace = necklace + necklace
left  = [[0,0] for i in range(2*N+1)]
right = [[0,0] for i in range(2*N+1)]

for i in range(1, 2*N+1):
    c = necklace[i-1]
    if c == 'r':
        left[i][0] = left[i-1][0] + 1
        left[i][1] = 0
    elif c == 'b':
        left[i][1] = left[i-1][1] + 1
        left[i][0] = 0
    else:
        left[i][0] = left[i-1][0] + 1
        left[i][1] = left[i-1][1] + 1

for i in range(2*N-1, -1, -1):
    c = necklace[i]
    if c == 'r':
        right[i][0] = right[i+1][0] + 1
        right[i][1] = 0
    elif c == 'b':
        right[i][1] = right[i+1][1] + 1
        right[i][0] = 0
    else:
        right[i][0] = right[i+1][0] + 1
        right[i][1] = right[i+1][1] + 1


count = 0
for i in range(2*N):
    count = max(count, max(left[i][0], left[i][1]) + max(right[i][0], right[i][1]))
count = min(count, N)

fout.write(str(count) + '\n')

fin.close()
fout.close()
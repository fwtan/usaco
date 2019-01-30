"""
ID: fuwen.t1
LANG: PYTHON3
TASK: castle
"""

comp_id = 0
max_comp_size = -1
comp_to_size = {}
comp_pairs = {}


fin  = open('castle.in', 'r')
fout = open('castle.out', 'w')

M, N = map(int, fin.readline().rstrip().split())

grid, comp = [], []
for i in range(N):
    line = list(map(int, fin.readline().rstrip().split()))
    grid.append(line)
    comp.append([-1] * M)


def dfs(x, y, comp_id):
    comp[y][x] = comp_id
    comp_size = 1

    # west
    if x > 0:
        if grid[y][x] % 2 == 1:
            n_cid = comp[y][x-1]
            if n_cid > 0 and n_cid != comp_id:
                wall = comp_pairs.get((n_cid, comp_id), None)
                if wall is None:
                    comp_pairs[(n_cid, comp_id)] = (x-1, y, 'E')
                else:
                    # the more 'west' or 'south', the better
                    if x-1 < wall[0]:
                        comp_pairs[(n_cid, comp_id)] = (x-1, y, 'E')
                    elif (x-1 == wall[0]) and (y > wall[1]):
                        comp_pairs[(n_cid, comp_id)] = (x-1, y, 'E')
        elif comp[y][x-1] < 0:
            comp_size += dfs(x-1, y, comp_id)
    # east
    if x < M-1:
        if (grid[y][x] >> 2) % 2 == 1:
            # wall
            n_cid = comp[y][x+1]
            if n_cid > 0 and n_cid != comp_id:
                wall = comp_pairs.get((n_cid, comp_id), None)
                if wall is None:
                    comp_pairs[(n_cid, comp_id)] = (x, y, 'E')
                else:
                    if x < wall[0]:
                        comp_pairs[(n_cid, comp_id)] = (x, y, 'E')
                    elif (x == wall[0]) and (y > wall[1]):
                        comp_pairs[(n_cid, comp_id)] = (x, y, 'E')
        elif comp[y][x+1] < 0:
            comp_size += dfs(x+1, y, comp_id)
    # north
    if y > 0:
        if (grid[y][x] >> 1) % 2 == 1:
            # wall
            n_cid = comp[y-1][x]
            if n_cid > 0 and n_cid != comp_id:
                wall = comp_pairs.get((n_cid, comp_id), None)
                if wall is None:
                    comp_pairs[(n_cid, comp_id)] = (x, y, 'N')
                else:
                    if x < wall[0]:
                        comp_pairs[(n_cid, comp_id)] = (x, y, 'N')
                    elif (x == wall[0]) and y >= wall[1]:
                        comp_pairs[(n_cid, comp_id)] = (x, y, 'N')
        elif comp[y-1][x] < 0:
            comp_size += dfs(x, y-1, comp_id)
    # south
    if y < N-1:
        if (grid[y][x] >> 3) % 2 == 1:
            # wall
            n_cid = comp[y+1][x]
            if n_cid > 0 and n_cid != comp_id:
                wall = comp_pairs.get((n_cid, comp_id), None)
                if wall is None:
                    comp_pairs[(n_cid, comp_id)] = (x, y+1, 'N')
                else:
                    if x < wall[0]:
                        comp_pairs[(n_cid, comp_id)] = (x, y+1, 'N')
                    elif x == wall[0] and y+1 >= wall[1]:
                        comp_pairs[(n_cid, comp_id)] = (x, y+1, 'N')
        elif comp[y+1][x] < 0:
            comp_size += dfs(x, y+1, comp_id)
    return comp_size


for y in range(N):
    for x in range(M):
        if comp[y][x] < 0:
            comp_id += 1
            comp_size = dfs(x, y, comp_id)
            comp_to_size[comp_id] = comp_size
            max_comp_size = max(max_comp_size, comp_size)
        

fout.write(str(comp_id) + '\n')
fout.write(str(max_comp_size) + '\n')

max_merge_area = -1
location = (M+1, -1)
direction = None

for k, v in comp_pairs.items():
    merge_area = comp_to_size[k[0]] + comp_to_size[k[1]]
    if merge_area > max_merge_area:
        max_merge_area = merge_area
        location = (v[0]+1, v[1]+1)
        direction = v[2]
    elif merge_area == max_merge_area:
        if v[0]+1 < location[0]:
            location = (v[0]+1, v[1]+1)
            direction = v[2]
        elif v[0]+1 == location[0] and v[1]+1 > location[1]:
            location = (v[0]+1, v[1]+1)
            direction = v[2]
        elif v[0]+1 == location[0] and v[1]+1 == location[1] and v[2] == 'N':
            location = (v[0]+1, v[1]+1)
            direction = v[2]
                
fout.write(str(max_merge_area) + '\n')
fout.write('%d %d %s'%(location[1], location[0], direction) + '\n')

fin.close()
fout.close()
from heapq import heappush, heappop

"""
The main point is that the height of water on any given cell is equal to the minimum of the maximum
of the heights of all cells over all path from that cell to any cell on the boundary.
To find these values for all the cells, we use a min priority queue (heapq in a min heap) that initially add all the
boundary cells except the 4 corners in it with the height of the cell first (smaller height will give
it a higher priority). Then when one is pop, all its neighbours that have not been found yet
are suddenly included inside the priority queue (the four corners can be omitted from the graph).
To remember who was visited and the height of water + cell on each cell, use another matrix or
a dictionary.
"""

def find_neighbours(r,c,R,C):
    l_neighbs = []
    if r >0:
        l_neighbs.append([r-1,c])
    if c >0:
        l_neighbs.append([r,c-1])
    if r < R-1:
        l_neighbs.append([r+1, c])
    if c < C-1:
        l_neighbs.append([r, c+1])
    return l_neighbs

T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    R, C = map(int, input().split())

    cells_heights = [[0 for _1 in range(C)] for _2 in range(R)]
    for row in range(R):
        cells_heights[row] = list(map(int, input().split()))
    cells_water_heights = [[-1 for _1 in range(C)] for _2 in range(R)]
    # add the non-corner boundary vertices
    l_priority_height = []
    for r in range(1,R-1):
        heappush(l_priority_height, (cells_heights[r][0],r,0))
        cells_water_heights[r][0] = cells_heights[r][0]
        heappush(l_priority_height, (cells_heights[r][C-1], r, C-1))
        cells_water_heights[r][C-1] = cells_heights[r][C-1]
    for c in range(1,C-1):
        heappush(l_priority_height, (cells_heights[0][c], 0, c))
        cells_water_heights[0][c] = cells_heights[0][c]
        heappush(l_priority_height, (cells_heights[R-1][c], R-1, c))
        cells_water_heights[R-1][c] = cells_heights[R-1][c]
    cells_water_heights[0][0], cells_water_heights[R-1][0], cells_water_heights[0][C-1], cells_water_heights[R-1][C-1] = 0,0,0,0

    # Perform min priority queue to find water height on each cell and keep total of water in the process
    tot_water = 0
    while len(l_priority_height) > 0:
        (h,r,c) = heappop(l_priority_height)
        for n_r, n_c in find_neighbours(r,c,R,C):
            if cells_water_heights[n_r][n_c] == -1:
                heappush(l_priority_height, (cells_heights[n_r][n_c], n_r, n_c))
                cells_water_heights[n_r][n_c] = max(cells_heights[n_r][n_c], cells_water_heights[r][c])
                tot_water += cells_water_heights[n_r][n_c] - cells_heights[n_r][n_c]

    print("Case #{}: ".format(t) + str(tot_water))











"""
Here is another solution is not complete and it is probably too messy. The main point is that the height of water 
on any given cell is equal to the minimum of the maximum of the heights of all cells over all path from that cell to 
any cell on the boundary. To find these, I perform union of disjoint sets by order of the maximum heights of adjacent 
cells until each cell is connected to a cell on the boundary. But I guess there must be a simpler solution 
because this is messy


def getParent(coords, parent):
    (r,c) = coords
    # find parent and compress path
    if parent[r][c] != coords:
        parent[r][c] = getParent(parent[r][c], parent)
    return parent[r][c]

def merge(point1,point2, parent):
    (r1,c1), (r2,c2) = point1, point2
    par_1, par_2 = getParent((r1,c1), parent), getParent((r2,c2), parent)
    # merge two components
    # use union by rank heuristic
    if par_1 == par_2:
        return
    elif rank[par_1] >= rank[par_2]:
        parent[par_2[0],par_2[1]] = par_1
        if rank[par_1] == rank[par_2]:
            rank[par_1] += 1
    else:
        parent[par_1[0], par_1[1]] = par_2

T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    R, C = map(int, input().split())

    # Construct cells with disjoint sets
    mat_heights = [[0 for _1 in range(C)] for _2 in range(R)]
    for row in range(R):
        mat_heights[row] = list(map(int, input().split()))
    parent = [[(r, c) for c in range(C)] for r in range(R)]
    rank = [[1 for c in range(C)] for r in range(R)]

    # Construct graph but boundary cells have no edges between themselves
    l_edges = []
    for r in range(0,R-1):
        for c in range(1,C-1):
            top, bottom = (r,c), (r+1,c)
            v_top = mat_heights[r][c]
            v_bottom = mat_heights[r+1][c]
            if v_top > v_bottom:
                v_1, v_2 = v_top, v_bottom
                pair_1, pair_2 = top, bottom
            else:
                v_1, v_2 = v_bottom, v_top
                pair_1, pair_2 = bottom, top
            l_edges.append((v_1, v_2, pair_1, pair_2))
    for r in range(1,R-1):
        for c in range(0,C-1):
            left, right = (r,c), (r,c+1)
            v_left = mat_heights[r][c]
            v_right = mat_heights[r+1][c]
            if v_left > v_right:
                v_1, v_2 = v_left, v_right
                pair_1, pair_2 = left, right
            else:
                v_1, v_2 = v_right, v_left
                pair_1, pair_2 = right, left
            l_edges.append((v_1, v_2, pair_1, pair_2))
    # Order edges by pair of heights where the max height is first,
    l_edges.sort()


    # Perform union of disjoint sets where each cell is a disjoint set at the start
    # until each interior cell is connected to a single cell on the outside
    # and each connected component is a tree
    for edge in l_edges:
        (val_1, val_2, point_1, point_2) = edge
        merge(point_1, point_2, parent)

    # Perform the bfs on trees or another recursive structure to calculate the amount
    # of water on each cell (which is equal to the maximum height of all the cells
    # between that wanted cell and the one on the boundary that is connected to it,
    # minus the height of the wanted cell)
"""
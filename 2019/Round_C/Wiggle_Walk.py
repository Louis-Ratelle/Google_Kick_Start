#moves_id = {"N":0, "E":1, "S":2, "O":3}
actual_mode = {"N":(-1,0), "E":(0,1), "S":(1,0), "W":(0,-1)}

# Find the non-visited squares of the (4) squares all the 4 directions and adjust them for deletion
def all_4_directions(d_neighbours_pos, cur_r, cur_c):

    north = d_neighbours_pos.get((cur_r, cur_c, "N"), (cur_r-1, cur_c))
    east = d_neighbours_pos.get((cur_r, cur_c, "E"), (cur_r, cur_c+1))
    south = d_neighbours_pos.get((cur_r, cur_c, "S"), (cur_r+1, cur_c))
    west = d_neighbours_pos.get((cur_r, cur_c, "W"), (cur_r, cur_c-1))

    d_neighbours_pos[(north[0], north[1], "S")] = south
    d_neighbours_pos[(south[0], south[1], "N")] = north
    d_neighbours_pos[(east[0], east[1], "W")] = west
    d_neighbours_pos[(west[0], west[1], "E")] = east


T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    N, R, C, SR, SC = map(int, input().split())
    S = input()
    d_neighbours_pos = {}

    cur_r = SR
    cur_c = SC
    for char in S:
        # Find next spot
        #id_m = moves_id[char]
        if (cur_r, cur_c, char) in d_neighbours_pos:
            (next_r, next_c) = d_neighbours_pos[(cur_r, cur_c, char)]
        else:
            m = actual_mode[char]
            (next_r, next_c) = (cur_r + m[0], cur_c + m[1])

        # Delete old spot and update neighbours
        all_4_directions(d_neighbours_pos, cur_r, cur_c)
        (cur_r, cur_c) = (next_r, next_c)

    print("Case #{}: ".format(t) + str(cur_r) + " " + str(cur_c))
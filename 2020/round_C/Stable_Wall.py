# Want to use topological sort that count incoming edges for each char. If this is a cycle, return impossible,
# otherwise return sort.

from collections import deque
from collections import defaultdict
import random

def count_incoming_edges(adj, s_chars):
    c_i_e = defaultdict(int)
    for u in s_chars:
        for v in adj[u]:
            c_i_e[v] += 1
    return c_i_e

def toposort(adj, s_chars):
    c_i_e = count_incoming_edges(adj, s_chars)
    order = []
    q = deque()
    # first take vertices with no incoming edges
    for u in s_chars:
        if c_i_e[u] == 0:
            q.append(u)
    # perform topological sort
    while len(q)> 0:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            c_i_e[v] -= 1
            if c_i_e[v] == 0:
                q.append(v)
    #print(order)
    if len(order)<len(s_chars):
        return -1
    return "".join(order)

def construct_graph(mat, rows, cols):
    s_chars = set()
    for r in range(rows):
        for c in range(cols):
            s_chars.add(mat[r][c])
    adj = {}
    for char in s_chars:
        adj[char] = set()
    for r in range(1, rows):
        for c in range(cols):
            if mat[r][c] != mat[r-1][c]:
                adj[mat[r][c]].add(mat[r-1][c])
    return s_chars, adj

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        rows, cols = list(map(int, input().split()))
        #rows, cols = 4,4
        mat = []
        sequence = ["a", "b", "c", "d", "e","f", "g", "h"]
        for r in range(rows):
            mat.append(input())
            #mat.append("".join([random.choice(sequence) for _ in range(cols)]))
        s_chars, adj = construct_graph(mat, rows, cols)
        sol = toposort(adj, s_chars)
        if sol == -1:
            print("Case #{}: ".format(t) + str(sol))
        else:
            print("Case #{}: ".format(t) + sol)




"""
4
4 6
ZOAAMM
ZOAOMM
ZOOOOM
ZZZZOM
4 4
XXOO
XFFO
XFXO
XXXO
5 3
XXX
XPX
XXX
XJX
XXX
3 10
AAABBCCDDE
AABBCCDDEE
AABBCCDDEE
"""

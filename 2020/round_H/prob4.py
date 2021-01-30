from collections import deque, defaultdict

def solution(N, Q, words, queries):
    #adj = defaultdict(set) # from letter to neighbors
    adj_mat = [[0 for j in range(26)] for i in range(26)]
    n = len(words)
    ord_A = ord("A")
    words = [[ord(char) - ord_A for char in words[pos]] for pos in range(n)]
    for lw in words:
        for c1 in lw:
            for c2 in lw:
                adj_mat[c1][c2] = 1

    # do BFS for each char to construct distance between chars
    mat_dist = [[30 for j in range(26)] for i in range(26)]
    for start in range(26):
        q = deque()
        q.append(start)
        dist_start = {}
        dist_start[start] = 2
        mat_dist[start][start] = 2
        while len(q) > 0:
            char = q.popleft()
            for neigh in range(26):
                if adj_mat[start][neigh] == 1 and neigh not in dist_start:
                    q.append(neigh)
                    dist_start[neigh] = dist_start[char] + 1
                    mat_dist[start][neigh] = dist_start[neigh]

    # Now do the queries using dist_pairs
    sol = []
    for [i1, i2] in queries:
        val = (min(mat_dist[i][j] for i in words[i1-1] for j in words[i2-1]))
        if val == 30:
            sol.append(-1)
        else:
            sol.append(val)
    return list(map(str,sol))

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        [N,Q] = list(map(int, input().split()))
        words = list(input().split())
        queries = []
        for _ in range(Q):
            queries.append(list(map(int, input().split())))
        sol = " ".join(solution(N, Q, words, queries))
        print("Case #{}: ".format(t) + sol)
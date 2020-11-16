from collections import deque, defaultdict

def solution(N, Q, words, queries):
    adj = defaultdict(set) # from letter to neighbors
    #for w in words:
        #for char1 in w:
            #for char2 in w:
                #adj[char1].add(char2)
    [adj[char1].add(char2) for w in words for char1 in w for char2 in w]

    # do BFS for each char to construct distance between chars
    d = {}
    for start in adj:
        q = deque()
        q.append(start)
        dist_start = {}
        dist_start[start] = 0
        d[(start, start)] = -2
        while len(q) > 0:
            char = q.popleft()
            for neigh in adj[char]:
                if neigh not in dist_start:
                    q.append(neigh)
                    dist_start[neigh] = dist_start[char] - 1
                    d[(start, neigh)] = dist_start[neigh]
    for char1 in adj:
        for char2 in adj:
            if (char1, char2) not in d:
                d[(char1, char2)] = 1

    # Now do the queries using dist_pairs
    sol = []
    for [i1, i2] in queries:
        sol.append(-min(d[(c1,c2)] for c1 in words[i1-1] for c2 in words[i2-1] ) )
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
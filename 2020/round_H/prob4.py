# Solution only for the first testing set

from collections import deque, defaultdict

def solution(N, Q, words, queries):

    adj_words= defaultdict(list)

    for w1 in words:
        s1 = set([char for char in w1])
        for w2 in words:
            s2 = set([char for char in w2])
            if len(s1.intersection(s2)):
                adj_words[w1].append(w2)

    dist_words = {}
    for start in words:
        q = deque()
        q.append(start)
        dist_start = {}
        dist_start[start] = 0
        dist_words[(start, start)] = 0
        while len(q) > 0:
            w = q.popleft()
            for neigh in adj_words[w]:
                if neigh not in dist_start:
                    q.append(neigh)
                    dist_start[neigh] = dist_start[w] + 1
                    dist_words[(start,neigh)] = dist_start[neigh]

    sol = []
    for [i1, i2] in queries:
        w1 = words[i1-1]
        w2 = words[i2-1]
        if (w1,w2) not in dist_words:
            sol.append(-1)
        else:
            sol.append(dist_words[(w1,w2)] + 1)

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
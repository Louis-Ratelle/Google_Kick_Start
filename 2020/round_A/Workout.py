import heapq
import math

def solution(l,N,K):
    h = []
    for i in range(1,N):
        val = l[i]-l[i-1]
        if val > 1:
            h.append((-val, 0, val))
    heapq.heapify(h)
    for i in range(K):
        if len(h)==0:
            return 1
        neg_dist, nb_sep, orig_dist = heapq.heappop(h)
        if nb_sep < orig_dist-1:
            heapq.heappush(h, (-math.ceil(orig_dist/(nb_sep+2)), nb_sep+1, orig_dist))
    if len(h) == 0:
        return 1
    neg_dist, nb_sep, orig_dist = heapq.heappop(h)
    return -neg_dist

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, K = list(map(int, input().split()))
        l = list(map(int, input().split()))
        sol = solution(l,N,K)
        print("Case #{}: ".format(t) + str(sol))
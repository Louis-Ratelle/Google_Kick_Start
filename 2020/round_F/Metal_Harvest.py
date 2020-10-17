import math

def min_cover(intervals, N, K):
    if len(intervals) == 0:
        return 0
    end_cover = 0
    sol = 0
    for [S, E] in intervals:
        if end_cover < E:
            left = max(end_cover, S)
            new_covs = math.ceil((E-left)/K)
            sol += new_covs
            end_cover = left + new_covs * K
    return sol

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        [N,K] = list(map(int, input().split()))
        intervals = []
        for _ in range(N):
            intervals.append(list(map(int, input().split())))
        intervals.sort()
        sol = min_cover(intervals, N, K)
        print("Case #{}: ".format(t) + str(sol))
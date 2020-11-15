
def solution(N,K,S):
    return min(K + N, K + K - S + N-S)





if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        [N,K,S] = list(map(int, input().split()))
        sol = str(solution(N,K,S))
        print("Case #{}: ".format(t) + sol)
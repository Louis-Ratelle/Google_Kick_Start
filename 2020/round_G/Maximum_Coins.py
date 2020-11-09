def solution(mat, N):
    sol = 0
    for diff in range(N):
        sol = max(sol, sum([mat[i][i+diff] for i in range(N-diff)]) )
    for diff in range(1,N):
        sol = max(sol, sum([mat[i+diff][i] for i in range(N-diff)]) )
    return sol

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        mat = []
        for _ in range(N):
            mat.append(list(map(int, input().split())))
        sol = solution(mat, N)
        print("Case #{}: ".format(t) + str(sol))
def solution(l, N, D):
    l.reverse()
    sol = D
    for mult_ in l:
        sol = (sol//mult_) * mult_
    return sol

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, D = list(map(int, input().split()))
        l = list(map(int, input().split()))
        sol = solution(l, N, D)
        print("Case #{}: ".format(t) + str(sol))
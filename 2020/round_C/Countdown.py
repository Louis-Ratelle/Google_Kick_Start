def calc_countdown(l,K):
    l.reverse()
    n = len(l)
    sol = 0
    for i in range(n-K+1):
        correct = True
        for j in range(K):
            if l[i+j] != j+1:
                correct = False
                break
        if correct:
            sol += 1
    return sol

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, K = list(map(int, input().split()))
        l = list(map(int, input().split()))
        sol = calc_countdown(l, K)
        print("Case #{}: ".format(t) + str(sol))
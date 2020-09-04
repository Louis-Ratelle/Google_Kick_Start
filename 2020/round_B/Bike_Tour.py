def count_peaks(l, N):
    sol = 0
    for i in range(1, N-1):
        if l[i-1] < l[i] and l[i] > l[i+1]:
            sol += 1
    return sol


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        l = list(map(int, input().split()))
        sol = count_peaks(l, N)
        print("Case #{}: ".format(t) + str(sol))
def sum_stacks(stacks):
    cumul = []
    for st in stacks:
        l = [0]
        for elem in st:
            l.append(elem + l[-1])
        cumul.append(l)
    return cumul


def buy_max_plates(stacks, N, K, P):
    cumul = sum_stacks(stacks)
    l = [0 for _ in range(P+1)]
    l_old = [0 for _ in range(P+1)]
    for pos_stack in range(N):
        l_old = l
        l = [0 for _ in range(P+1)]
        st = cumul[pos_stack]
        for p in range(1, P+1):
            temp = []
            for x in range(min(p+1,K+1)):
                st[x]
                temp.append(st[x] + l_old[p-x])
            l[p] = max(temp)

    return max(l)


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, K, P = list(map(int, input().split()))
        stacks = []
        for _ in range(N):
            stacks.append(list(map(int, input().split())))
        sol = buy_max_plates(stacks, N, K, P)
        print("Case #{}: ".format(t) + str(sol))
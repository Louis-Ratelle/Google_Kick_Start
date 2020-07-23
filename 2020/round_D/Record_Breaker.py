T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nb_visitors = list(map(int, input().split()))
    l_max = [nb_visitors[0]]
    bool_max = [True]
    for elem in nb_visitors[1:]:
        if l_max[-1] < elem:
            bool_max.append(True)
        else:
            bool_max.append(False)
        l_max.append(max(l_max[-1], elem))

    sol = 0
    for i in range(N-1):
        if bool_max[i] and nb_visitors[i] > nb_visitors[i+1]:
            sol += 1
    if bool_max[-1]:
        sol += 1
    print("Case #{}: ".format(t) + str(sol))
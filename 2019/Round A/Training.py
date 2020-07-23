T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    N, P = map(int, input().split())
    l_skills = list(map(int, input().split()))
    l_skills.sort()
    l_sum_P_trailing = [0 for _ in range(N)]
    tot = sum(l_skills[0:P])
    l_sum_P_trailing[P-1] = tot
    for pos in range(P, N):
        tot = tot + l_skills[pos] - l_skills[pos-P]
        l_sum_P_trailing[pos] = tot
    min_training = 10**10
    for pos in range(P-1, N):
        min_training = min(min_training, P * l_skills[pos] - l_sum_P_trailing[pos])
    print("Case #{}: ".format(t) + str(min_training))
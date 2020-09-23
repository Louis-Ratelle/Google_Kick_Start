T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    N, Q = map(int, input().split())
    A = input()
    l_Q = []
    for _ in range(Q):
        l_Q.append(list(map(int, input().split())))
    mat = [[0 for _1 in range(26)]]
    for char in A:
        mat.append(mat[-1][0:])
        mat[-1][ord(char)-65] += 1

    sol = 0
    for q in l_Q:
        left = q[0]
        right = q[1]
        count_odd = 0
        for li, ri in zip(mat[left-1], mat[right]):
            if ((ri-li)%2) == 1:
                count_odd += 1
        if count_odd <= 1:
            sol+=1

    print("Case #{}: ".format(t) + str(sol))
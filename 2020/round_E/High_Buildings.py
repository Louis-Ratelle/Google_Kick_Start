def list_of_buildings(N,A,B,C):

    remaind =  N - ((A-C)+(B-C)+C)
    if remaind < 0:
        return "IMPOSSIBLE"
    elif N == C:
        return " ".join(["1"]*N)
    elif N == 1:
        return "1"
    elif A == B == C == 1:
        return "IMPOSSIBLE"
    elif N ==2:
        l = []
        l += [1] * (A - C)
        l += [2] * C
        l += [1] * (B - C)
        return " ".join(map(str, l))
    else:
        l = []
        l += [2]*(A-C)
        l += [3]*C
        l += [2]*(B-C)
        l = l[0:1] + [1]*remaind + l[1:]
        return " ".join(map(str, l))

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        [N,A,B,C] = list(map(int, input().split()))
        sol = list_of_buildings(N,A,B,C)
        #sol = " ".join(map(str, list_of_buildings(N,A,B,C)))
        print("Case #{}: ".format(t) + sol)
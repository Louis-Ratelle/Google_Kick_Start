from collections import defaultdict
import math

def order(N,X,A):
    d = defaultdict(list)
    for i, elem in enumerate(A):
        d[math.ceil(elem/X)].append(str(i+1))
    keys = list(d.keys())
    keys.sort()
    sol = []
    for key in keys:
        sol += d[key]
    return " ".join(sol)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        [N,X] = list(map(int, input().split()))
        A = list(map(int, input().split()))
        sol = order(N,X,A)
        print("Case #{}: ".format(t) + sol)
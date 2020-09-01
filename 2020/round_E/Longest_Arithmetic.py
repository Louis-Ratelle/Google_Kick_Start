def longest_contig_arithm_exp(l):
    sol = 2
    length = 1
    diff = None
    pos = 0
    while pos < len(l) - 1:
        if diff is None:
            diff = l[pos+1] - l[pos]
            length = 2
            pos += 1
        elif l[pos+1] - l[pos] == diff:
            length += 1
            pos += 1
        else:
            diff = None
            length = 1
        sol = max(sol, length)

    return sol

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        l = list(map(int, input().split()))
        sol = longest_contig_arithm_exp(l)
        print("Case #{}: ".format(t) + str(sol))
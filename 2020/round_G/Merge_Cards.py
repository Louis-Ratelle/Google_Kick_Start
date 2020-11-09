from collections import defaultdict

def compute_all_expected_appearances(max_ = 5000):
    d = defaultdict(list)
    d[1] = [0,0]
    d[2] = [0,1,1]
    for i in range(3,max_+1):
        d[i] = [0]
        for j in range(1,i+1):
            if j == 1:
                d[i].append(1/(i-1) + d[i-1][1])
            elif j == i:
                d[i].append(1 / (i - 1) + d[i - 1][i-1])
            else:
                d[i].append((1/(i-1)) * 2 + ((j-1)/(i-1))*d[i-1][j-1] + ((i-j)/(i-1))*d[i-1][j])
    return d

def solution(d ,seq, N):
    sol = 0
    return sum([seq[pos] * d[N][pos+1] for pos in range(N)])

if __name__ == '__main__':
    T = int(input())
    d = compute_all_expected_appearances()
    for t in range(1, T + 1):
        N = int(input())
        seq = list(map(int, input().split()))
        sol = solution(d ,seq, N)
        print("Case #{}: ".format(t) + str(sol))
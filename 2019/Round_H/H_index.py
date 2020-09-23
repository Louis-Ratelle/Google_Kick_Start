from collections import defaultdict

def H_index(l, N):
    cur_H_ind = 1
    count_over_cur_index = 1
    d = defaultdict(int)
    d[l[0]] += 1
    sol = [1]
    for i in range(1,N):
        elem = l[i]
        d[elem]+=1
        if elem >= cur_H_ind:
            count_over_cur_index += 1
        if count_over_cur_index - d[cur_H_ind] >= cur_H_ind + 1:
            count_over_cur_index = count_over_cur_index - d[cur_H_ind]
            cur_H_ind += 1
        sol.append(cur_H_ind)
        sol = [str(elem) for elem in sol]
    return " ".join(sol)


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        l = list(map(int, input().split()))
        sol = H_index(l, N)
        print("Case #{}: ".format(t) + str(sol))
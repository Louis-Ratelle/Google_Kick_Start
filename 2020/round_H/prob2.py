def boring_up_to(num):
    if num == 0:
        return 0
    if num <= 9:
        return (num+1) // 2
    st = str(num)
    size = len(st)
    tot = 0

    # first part
    tot += sum([5**i for i in range(1,size)])

    # second part
    tot += 5**(size-1) * ((int(st[0]))//2)

    # third part
    for pos, s_dig in enumerate(st):
        dig = int(s_dig)
        if dig % 2 != (pos+1) % 2:
            break
        if pos == len(st)-1:
            tot+=1
        else:
            next_dig = int(st[pos+1])
            if (pos+1) % 2 == 1: # that means I want even at pos +1
                tot += (next_dig + 1)//2 * 5**(size-pos-2)
            else:
                tot += (next_dig) // 2 * 5 ** (size - pos - 2)
    return tot

def solution(L, R):
    if L == 1:
        before_L = 0
    else:
        before_L = boring_up_to(L-1)
    up_to_R = boring_up_to(R)
    return up_to_R - before_L

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        [L, R] = list(map(int, input().split()))
        sol = str(solution(L,R))
        print("Case #{}: ".format(t) + sol)
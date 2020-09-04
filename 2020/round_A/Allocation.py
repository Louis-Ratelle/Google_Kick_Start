import heapq

def solution(l, B):
    heapq.heapify(l)
    sol = 0
    while B >0 and len(l)>0:
        house_price = heapq.heappop(l)
        if house_price <= B:
            B -= house_price
            sol += 1
        else:
            break
    return sol


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, B = list(map(int, input().split()))
        l = list(map(int, input().split()))
        sol = solution(l, B)
        print("Case #{}: ".format(t) + str(sol))
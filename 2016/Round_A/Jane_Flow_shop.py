# from decimal import *, # getcontext().prec = 200, Decimal(1)/ Decimal(7)

def calculate_rest(r, l):
    tot = -l[0]
    for amount in l[1:]:
        tot = tot * (1+r) + amount
    return tot

def binary_search_interests(l):
    left, right = -1, 1
    # write your code here
    while abs(left-right) > 10**(-8):
        r = (left + right)/2
        rest = calculate_rest(r, l)
        if rest < 0:
            right = r
        elif rest > 0:
            left = r
        else:
            return r
    return (left + right) /2

T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    M = int(input())
    l_months = list(map(int, input().split()))
    result = binary_search_interests(l_months)
    print("Case #{}: ".format(t) + str(result))
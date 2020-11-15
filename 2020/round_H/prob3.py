def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

def horiz_dist(xs, start_x):
    return sum([abs(xs[i] - (start_x + i)) for i in range(len(xs))])

def solution(N,points):
    # in y easy, just find median in y and find sum of y distances
    ys = [pair[1] for pair in points]
    ys.sort() # could do faster by finding median
    median_y = ys[N//2]
    dist_y = sum([abs(y-median_y) for y in ys])


    # in x harder, need to use binary search
    xs = [pair[0] for pair in points]
    xs.sort()
    left = xs[0] - N # left of first pos in x
    right = xs[-1] + 1 # right if first pos in y
    while left + 1 < right:
        mid = (left + right) // 2
        tot_sign = sum([-sign(xs[i] - (mid + i)) for i in range(N)])
        if tot_sign <= 0:
            left = mid
        elif tot_sign > 0:
            right = mid
    dist_x = min(horiz_dist(xs, left), horiz_dist(xs, right))
    #print(left, right)
    #(dist_y, dist_x)
    return dist_y + dist_x

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        points = [list(map(int, input().split())) for _ in range(N)]
        sol = str(solution(N,points))
        print("Case #{}: ".format(t) + sol)


"""
1
2
1 1
4 4

"""
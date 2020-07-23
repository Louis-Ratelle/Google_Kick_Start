# Ne marche pas le mode interactif celui-là, uniquement avec python testing_tool.py python Number_Guessing.py

import sys

def ask_digit(i):
    print(i)
    sys.stdout.flush()
    answer = input()
    return answer

def binary_search(left, right):
    while left <= right: # This procedure assumes the number is always there
        middle = (left + right)//2
        answer = ask_digit(middle)
        if answer=="TOO_SMALL":
            left = middle + 1
        elif answer == "TOO_BIG":
            right = middle - 1
        else: # that means the number was found
            return


T = int(input())
for t in range(1, T+1):
    left, right = map(int, input().split())
    left += 1
    N = int(input())
    binary_search(left, right)
    #print("".join([str(elem) for elem in seq]))
    #sys.stdout.flush()
    #verdict = input()
    #if verdict == "N":
#       sys.exit()
sys.exit()
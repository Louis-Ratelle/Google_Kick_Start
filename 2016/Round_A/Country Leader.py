from collections import defaultdict

def count_different_letters(word):
    d = set()
    for char in word:
        d.add(char)
    return len(d)

def find_max_element_lexicographic(l):
    mi = l[0]
    for name in l[1:]:
        if name < mi:
            mi = name
    return mi

T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    A = int(input())
    l_just_letters = []
    l_names = []
    for _ in range(A):
        word = input()
        l_names.append(word)
        l_just_letters.append("".join(word.split()))
    d_count_diff_letters = defaultdict(list)
    for name, concat in zip(l_names, l_just_letters):
        d_count_diff_letters[count_different_letters(concat)].append(name)
    l_max_names = d_count_diff_letters[max(d_count_diff_letters.keys())]
    result = find_max_element_lexicographic(l_max_names)
    print("Case #{}: ".format(t) + str(result))
class Fenwick:
    """maintains a tree to allow quick updates and queries
    """
    def __init__(self, t):
        """stores a table t and allows updates and queries
        of prefix sums in logarithmic time.
        :param array t: with numerical values
        """

        # this is faster O(len(t)) instead of O(len(t) log(len(t)))
        self.s = [0] + t[:]
        for i in range(1, len(self.s)-1):
            p = i + (i & -i)
            if p < len(self.s):
                self.s[p] = self.s[p] + self.s[i]

    # pylint: disable=redefined-builtin
    def prefixSum(self, a):
        """
        :param int a: index in t, negative a will return 0
        :returns: t[0] + ... + t[a]
        """
        i = a + 1                  # internal index starts at 1
        total = 0
        while i > 0:               # loops over neighbors
            total += self.s[i]     # cumulative sum
            i -= (i & -i)          # left neighbor
        return total

    def intervalSum(self, a, b):
        """
        :param int a b: with 0 <= a <= b
        :returns: t[a] + ... + t[b]
        """
        return self.prefixSum(b) - self.prefixSum(a-1)

    def add(self, a, val):
        """
        :param int a: index in t
        :modifies: adds val to t[a]
        """
        i = a + 1                  # internal index starts at 1
        while i < len(self.s):     # loops over parents
            self.s[i] += val       # update node
            i += (i & -i)          # parent

# snip}


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, opers = list(map(int, input().split()))
        vals = list(map(int, input().split()))
        seqs = []
        sol = 0
        for oper in range(opers):
            l = list(input().split())
            l[1] = int(l[1])-1
            if l[0] == "Q":
                l[2] = int(l[2])-1
            else:
                l[2] = int(l[2])
            seqs.append(l)

        vals1 = [elem if (pos % 2) == 0 else -elem for pos, elem in enumerate(vals)]
        tree1 = Fenwick(vals1)
        vals2 = [(pos+1)*elem if (pos % 2) == 0 else -(pos+1)*elem for pos, elem in enumerate(vals)]
        tree2 = Fenwick(vals2)

        for triple in seqs:
            #print(triple)
            if triple[0] == "Q":
                if (triple[1] % 2) == 0:
                    sol += tree2.intervalSum(triple[1], triple[2]) - tree1.intervalSum(triple[1], triple[2]) * (triple[1])
                else:
                    sol -= tree2.intervalSum(triple[1], triple[2]) - tree1.intervalSum(triple[1], triple[2]) * (triple[1])
            else:
                #print(triple)
                j = triple[1]
                new_val_j = triple[2]
                diff = new_val_j - vals[j]
                vals[j] = new_val_j
                if (j % 2) == 1:
                    diff = - diff
                tree1.add(j,diff)
                tree2.add(j,diff*(j+1))

        print("Case #{}: ".format(t) + str(sol))



        """
        
        
1
5 2
1 3 9 8 2
Q 2 4
Q 5 5
"""
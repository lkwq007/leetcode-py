class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        term=10**9+7
        acc=3
        for i in range(m-1):
            acc*=2
        for i in range(n-1):
            same,diff=acc,acc
            for j in range(m-1):
                same,diff=1*same+diff,2*diff+same
            acc=(same+diff)%term
        return acc
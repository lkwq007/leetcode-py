class Solution:
    def fib(self, N: int) -> int:
        if N<1:
            return 0
        last=0
        cur=1
        for i in range(N-1):
            last,cur=cur,last+cur
        return cur
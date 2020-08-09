class Solution:
    def clumsy(self, N: int) -> int:
        res=N%4
        rest=[0,-1,-2*1,-3*2][res]
        total=0
        for i in range(N,3,-4):
            
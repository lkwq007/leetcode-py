class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if len(A)<1 or len(A[0])<1:
            return 0
        h=len(A)
        w=len(A[0])
        for y in range(1,h):
            A[y][0]=A[y][0]+min(A[y-1][0],A[y-1][1])
            if w>1:
                A[y][-1]=A[y][-1]+min(A[y-1][-1],A[y-1][-2])
            for x in range(1,w-1):
                A[y][x]=A[y][x]+min(A[y-1][x-1],A[y-1][x],A[y-1][x+1])
        return min(A[h-1])
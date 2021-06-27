class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # boundary to center
        dp={}
        for idx in range(m):
            dp[(idx,-1,0)]=1
            dp[(idx,n,0)]=1
        for idx in range(n):
            dp[(-1,idx,0)]=1
            dp[(m,idx,0)]=1
        offset=[(1,0),(-1,0),(0,-1),(0,1)]
        term=10**9+7
        for k in range(N):
            for y in range(m):
                for x in range(n):
                    for yo,xo in offset:
                        yn=y+yo
                        xn=x+xo
                        dp[(y,x,k+1)]=(dp.get((y,x,k+1),0)+dp.get((yn,xn,k),0))%term
        return sum([dp.get((i,j,idx),0) for idx in range(1,N+1)])%term
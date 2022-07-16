class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # 1 <= m, n <= 1000
        matrix=grid
        if len(matrix)<1 or len(matrix[0])<1:
            return 0
        h=len(matrix)
        w=len(matrix[0])
        dp=[[-1]*w for _ in range(h)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        term=10**9+7
        def dfs(y0,x0):
            if dp[y0][x0]!=-1:
                return dp[y0][x0]
            ret=1
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=x1<w and 0<=y1<h:
                    if matrix[y1][x1]>matrix[y0][x0]:
                        if dp[y1][x1]!=-1:
                            ret+=dp[y1][x1]
                        else:
                            ret+=dfs(y1,x1)
            dp[y0][x0]=ret
            return ret
        ret=0
        for y in range(h):
            for x in range(w):
                if dp[y][x]==-1:
                    dfs(y,x)
                ret+=dp[y][x]
                ret%=term
        return ret
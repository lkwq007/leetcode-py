class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix)<1 or len(matrix[0])<1:
            return 0
        ret=0
        h=len(matrix)
        w=len(matrix[0])
        max_inc=[[-1]*w for _ in range(h)]
        max_dec=[[-1]*w for _ in range(h)]
        dp=[max_inc,max_dec]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(y0,x0,mode):
            if dp[mode][y0][x0]!=-1:
                return dp[mode][y0][x0]
            ret=0
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=x1<w and 0<=y1<h:
                    if mode==0 and matrix[y1][x1]>matrix[y0][x0]:
                        ret=max(ret,dfs(y1,x1,mode)+1)
                    elif mode==1 and matrix[y1][x1]<matrix[y0][x0]:
                        ret=max(ret,dfs(y1,x1,mode)+1)
            dp[mode][y0][x0]=ret
            return ret
        for y in range(h):
            for x in range(w):
                for mode in range(2):
                    if dp[mode][y][x]==-1:
                        dfs(y,x,mode)
                ret=max(dp[0][y][x]+dp[1][y][x]+1,ret)
        return ret

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix)<1 or len(matrix[0])<1:
            return 0
        ret=0
        h=len(matrix)
        w=len(matrix[0])
        max_inc=[[-1]*w for _ in range(h)]
        max_dec=[[-1]*w for _ in range(h)]
        dp=[max_inc,max_dec]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(y0,x0,mode):
            if dp[mode][y0][x0]!=-1:
                return dp[mode][y0][x0]
            ret=0
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=x1<w and 0<=y1<h:
                    if mode==0 and matrix[y1][x1]>matrix[y0][x0] or (mode==1 and matrix[y1][x1]<matrix[y0][x0]):
                        if dp[mode][y1][x1]!=-1:
                            ret=max(ret,dp[mode][y1][x1]+1)
                        else:
                            ret=max(ret,dfs(y1,x1,mode)+1)
            dp[mode][y0][x0]=ret
            return ret
        for y in range(h):
            for x in range(w):
                for mode in range(2):
                    if dp[mode][y][x]==-1:
                        dfs(y,x,mode)
                ret=max(dp[0][y][x]+dp[1][y][x]+1,ret)
        return ret
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        h=len(matrix)
        w=len(matrix[0])
        template=[0]*(w+1)
        dp=[template[:] for _ in range(h+1)]
        for y in range(h):
            acc=0
            for x in range(w):
                acc+=matrix[y][x]
                dp[y][x]=acc
        for x in range(w):
            acc=0
            for y in range(h):
                acc+=dp[y][x]
                dp[y][x]=acc
        ret=None
        for y in range(h):
            for x in range(w):
                for yn in range(y+1):
                    for xn in range(x+1):
                        tmp=dp[y][x]-dp[yn-1][x]-dp[y][xn-1]+dp[yn-1][xn-1]
                        if tmp<=k:
                            if ret is None:
                                ret=tmp
                            ret=max(tmp,ret)
        return ret

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        h=len(matrix)
        w=len(matrix[0])
        template=[0]*w
        dp=[template[:] for _ in range(h)]
        dp[0][0]=1 if matrix[0][0]=="1" else 0
        for x in range(1,w):
            if matrix[0][x]=="1":
                dp[0][x]=1+dp[0][x-1]
        for y in range(1,h):
            if matrix[y][0]=="1":
                dp[y][0]=1+dp[y-1][0]
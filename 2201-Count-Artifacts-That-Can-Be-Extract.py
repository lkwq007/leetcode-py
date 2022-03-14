class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        state=[[0]*n for _ in range(n)]
        for r,c in dig:
            state[r][c]=1
        dp=[[0]*(n+1) for _ in range(n+1)]
        dp[0][0]=state[0][0]
        for i in range(1,n):
            dp[0][i]=dp[0][i-1]+state[0][i]
            dp[i][0]=dp[i-1][0]+state[i][0]
        for i in range(1,n):
            for j in range(1,n):
                dp[i][j]=state[i][j]+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]
        # print(state)
        # print(dp)
        ret=0
        for r0,c0,r1,c1 in artifacts:
            target=(r1-r0+1)*(c1-c0+1)
            total=dp[r1][c1]-dp[r1][c0-1]-dp[r0-1][c1]+dp[r0-1][c0-1]
            if total==target:
                ret+=1
        return ret
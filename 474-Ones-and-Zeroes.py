class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        lst=[]
        dp=[[0]*(n+1) for _ in range(m+1)]
        for item in strs:
            zero=0
            one=0
            for s in item:
                if s=="0":
                    zero+=1
                else:
                    one+=1
            if zero>m or one>n:
                continue
            # lst.append((zero,one))
            for i in range(m,zero-1,-1):
                for j in range(n,one-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zero][j-one]+1)
        return dp[m][n]
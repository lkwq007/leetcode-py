class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp
        lst1=[ord(item) for item in s1]
        lst2=[ord(item) for item in s2]
        total=sum(lst1)+sum(lst2)
        template=[0]*(len(lst2)+1)
        dp=[template[:] for _ in range(len(lst1)+1)]
        ret=0
        for i in range(1,len(lst1)+1):
            for j in range(1,len(lst2)+1):
                if lst1[i-1]==lst2[j-1]:
                    dp[i][j]=max(dp[i-1][j-1]+lst1[i-1]+lst2[j-1],dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                ret=max(ret,dp[i][j])
        return total-ret

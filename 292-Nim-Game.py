class Solution:
    def canWinNim(self, n: int) -> bool:
        if n<=3:
            return True
        dp=[False]*n
        for i in range(3):
            dp[i]=True
        for i in range(3,n):
            flag=False
            for j in range(1,4):
                if not dp[i-j]:
                    flag=True
            dp[i]=flag
        return dp[-1]

class Solution:
    def canWinNim(self, n: int) -> bool:
        x=n%4
        if x==0:
            return False
        return True
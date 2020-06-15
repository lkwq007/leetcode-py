class Solution:
    def divisorGame(self, N: int) -> bool:
        return N%2==0

class Solution:
    def divisorGame(self, N: int) -> bool:
        if N<2:
            return False
        dp=[False]*(N+1)
        dp[2]=True
        def judge(x):
            boudary=x//2
            for divisor in range(1,boudary):
                if x%divisor==0:
                    rest=x-divisor
                    if not dp[rest]:
                        flag=False
                        dp[x]=True
        for i in range(3,N+1):
            judge(i)
        return dp[N]
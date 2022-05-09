class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        term=10**9+7
        dp=[0]*(len(pressedKeys)+4)
        for i in range(1,5):
            dp[-i]=1
        for i,item in enumerate(pressedKeys):
            dp[i]+=dp[i-1]
            offset=4 if item in "79" else 3
            for j in range(i-1,max(-1,i-offset),-1):
                if pressedKeys[j]==item:
                    dp[i]+=dp[j-1]
                else:
                    break
            dp[i]%=term
        return dp[len(pressedKeys)-1]
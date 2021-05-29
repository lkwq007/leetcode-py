class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=="1":
            return False
        dp=[0]*(len(s)+1)
        dp[0]=1
        for i in range(1,len(s)):
            left=max(0,i-maxJump)-1
            right=i-minJump
            if right>=0 and dp[right]-dp[left]>0 and s[i]=="0":
                # reachable
                ret=True
                dp[i]=dp[i-1]+1
            else:
                ret=False
                dp[i]=dp[i-1]
            # print(i,ret)
        # print(dp)
        return ret
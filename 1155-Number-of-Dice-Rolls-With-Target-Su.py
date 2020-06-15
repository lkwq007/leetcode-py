class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target<d or d*f<target:
            return 0
        dp=[0]*(target+1)
        dp[d]=1
        dp[d*f]=1
        for idx in range(d+1,target):
            
        
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp=[0]*30000
        ret=1
        for val in reversed(arr):
            if -10000<=val+difference<=10000:
                dp[val]=dp[val+difference]+1
            else:
                dp[val]=1
            ret=max(ret,dp[val])
        return ret

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp={}
        ret=1
        for val in reversed(arr):
            dp[val]=dp.get(val+difference,0)+1
            ret=max(ret,dp[val])
        return ret
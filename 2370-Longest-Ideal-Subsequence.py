class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*26
        base=ord("a")
        for item in s:
            cur=ord(item)-base
            acc=0
            for i in range(max(0,cur-k),min(26,cur+k+1)):
                acc=max(acc,1+dp[i])
            dp[cur]=acc
        return max(dp)
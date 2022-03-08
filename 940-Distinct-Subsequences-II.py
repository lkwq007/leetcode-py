class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # dp
        term=10**9+7
        dp=[0]*len(s)
        last=[-1]*26
        for i in range(len(s)):
            item=ord(s[i])-ord("a")
            for j in range(26):
                if last[j]!=-1:
                    dp[i]+=dp[last[j]]
                if j==item:
                    dp[i]+=1
                dp[i]%=term
            last[item]=i
        return sum([dp[x] for x in last if x!=-1])%term

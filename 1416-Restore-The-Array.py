class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        term=10**9+7
        dp=[0]*(len(s)+1)
        dp[-1]=1
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                j=i
                while j<len(s):
                    cur=int(s[i:j+1])
                    if cur<=k:
                        dp[i]+=dp[j+1]
                        dp[i]%=term
                    else:
                        break
                    j+=1
        return dp[0]

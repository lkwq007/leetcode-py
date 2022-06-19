class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ret=0
        mask=1
        acc=0
        bound=1<<32
        for item in reversed(s):
            if item=="0":
                ret+=1
            elif mask<bound:
                acc+=mask
                if acc<=k:
                    ret+=1
            mask=mask<<1
        return ret
                
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ret=0
        record={}
        record[0]=0
        dp=[-1]*(len(s)+2)
        dp[0]=0
        for item in s:
            cur=int(item)
            for i in range(ret,-1,-1):
                if dp[i]==-1:
                    break
                val=dp[i]
                next=val*2+cur
                if next<=k and (dp[i+1]==-1 or dp[i+1]>next):
                    dp[i+1]=next
                    if i+1>ret:
                        ret=i+1
        return ret
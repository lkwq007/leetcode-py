class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        total=len(words[0])
        lst=[0]*total
        tbl=[lst[:] for _ in range(26)]
        base=ord("a")
        for word in words:
            for i in range(total):
                cur=ord(word[i])-base
                tbl[cur][i]+=1
        term=10**9+7
        last=[1]*(total+1)
        dp=[0]*(total+1)
        for i in range(len(target)):
            cur=ord(target[i])-base
            for j in range(total):
                dp[j]=dp[j-1]+tbl[cur][j]*last[j-1]
                dp[j]%=term
            last=dp
            dp=[0]*(total+1)
        return last[-2]
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        lst=[0]*(len(words[0])+1)
        prefix=[lst[:] for _ in range(26)]
        base=ord("a")
        for word in words:
            for i in range(len(word)):
                cur=ord(word[i])-base
                prefix[cur][i]+=1
        for i in range(len(prefix)):
            for j in range(len(prefix[i])):
                prefix[i][j]+=prefix[i][j-1]
        term=10**9+7
        import functools
        total=len(words[0])
        return probe(0,0)
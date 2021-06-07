class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ret=0
        for i in range(2,len(s)):
            if s[i]!=s[i-1] and s[i]!=s[i-2] and s[i-1]!=s[i-2]:
                ret+=1
        return ret
class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s)<2:
            return ""
        term=10**9+7
        base=ord("a")-1
        left=ord(s[0])-base
        right=ord(s[-1])-base
        if s[0]==s[-1]:
            ret=s[0]
        for i in range(1,len(s)-1):
            left=left*27+ord(s[i])-base
            right=
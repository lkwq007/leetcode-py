class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute force
        ret=0
        for i in range(len(s)):
            acc=1
            j=1
            while i-j>=0 and i+j<len(s) and s[i+j]==s[i-j]:
                acc+=1
                j+=1
            j=1
            while i-j+1>=0 and i+j<len(s) and s[i+j]==s[i-j+1]:
                acc+=1
                j+=1
            ret+=acc
        return ret
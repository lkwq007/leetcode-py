class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx=len(s)-1
        while idx>=0 and s[idx]==" ":
            idx-=1
        if idx<0:
            return 0
        end=idx
        while idx>=0 and s[idx]!=" ":
            idx-=1
        return end-idx
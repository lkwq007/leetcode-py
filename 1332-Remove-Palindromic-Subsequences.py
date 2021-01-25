class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s)<1:
            return 0
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-1-i]:
                return 2
        return 1
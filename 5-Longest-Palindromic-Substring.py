class Solution:
    def longestPalindrome(self, s: str) -> str:
        pos=0
        for idx in range(0,len(s)):
            
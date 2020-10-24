class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)<3:
            return True
        i=0
        while i<len(s)-1-i and s[i]==s[len(s)-i-1]:
            i+=1
        if i>=len(s)-1-i:
            return True
        # two cases
        left=i
        right=len(s)-i-1
        left+=1
        while left<right and s[left]==s[right]:
            left+=1
            right-=1
        if left>=right:
            return True
        left=i
        right=len(s)-i-1
        right-=1
        while left<right and s[left]==s[right]:
            left+=1
            right-=1
        if left>=right:
            return True
        return False
class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)==1:
            return 1
        left=0
        right=len(s)-1
        while left<right:
            if s[left]==s[right]:
                item=s[left]
                while left<=right and item==s[left]:
                    left+=1
                while left<=right and item==s[right]:
                    right-=1
            else:
                return right-left+1
        return 1 if left==right else 0
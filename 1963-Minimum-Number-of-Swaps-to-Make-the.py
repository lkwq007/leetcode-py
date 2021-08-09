class Solution:
    def minSwaps(self, s: str) -> int:
        left=0
        lcnt=0
        right=len(s)-1
        rcnt=0
        ret=0
        
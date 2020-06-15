class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return 1
        prev=1
        prev2=1
        idx=2
        while idx<=n:
            tmp=prev+prev2
            prev2=prev
            prev=tmp
            idx+=1
        return prev
        
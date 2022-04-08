class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x=start^goal
        ret=0
        while x>0:
            if x&1:
                ret+=1
            x=x>>1
        return ret
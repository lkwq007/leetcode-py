class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ret=0
        coins.sort()
        for c in coins:
            low=c
            high=c+ret
            if low<=ret+1:
                ret=high
            else:
                break
        return ret+1
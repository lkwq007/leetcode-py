class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        dp={}
        idx=1
        record={}
        
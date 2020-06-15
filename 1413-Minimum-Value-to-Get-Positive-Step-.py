class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val=0
        acc=0
        for item in nums:
            acc+=item
            min_val=min(acc,min_val)
        if min_val>=0:
            return 1
        return -min_val+1
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        term=10**9+7
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            nums[i]=acc
        # binary search
        ret=0
        for left in range(len(nums)):
            
        return 0
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ret=0
        acc=0
        last=nums[0]-1
        for i in range(len(nums)):
            if nums[i]>last:
                acc+=nums[i]
            else:
                acc=nums[i]
            ret=max(acc,ret)
            last=nums[i]
        return ret
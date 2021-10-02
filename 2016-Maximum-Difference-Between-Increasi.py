class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ret=-1
        acc=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>acc:
                ret=max(ret,nums[i]-acc)
            acc=min(acc,nums[i])
        return ret
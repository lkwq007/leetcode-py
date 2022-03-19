class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        idx0=0
        idx1=0
        for i in range(len(nums)):
            if nums[i]<nums[idx0]:
                idx0=i
            if nums[i]>nums[idx1]:
                idx1=i
        if idx0>idx1:
            idx0,idx1=idx1,idx0
        return min(idx1+1,len(nums)-idx0,idx0+1+len(nums)-idx1)
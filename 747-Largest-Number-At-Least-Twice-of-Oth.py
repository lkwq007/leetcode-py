class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        if nums[0]<nums[1]:
            idx=[1,0]
        else:
            idx=[0,1]
        for i in range(2,len(nums)):
            item=nums[i]
            if item>nums[idx[0]]:
                idx[1]=idx[0]
                idx[0]=i
            elif item>nums[idx[1]]:
                idx[1]=i
        if nums[idx[0]]>=nums[idx[1]]*2:
            return idx[0]
        return -1
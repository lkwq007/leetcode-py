class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<4:
            return 0
        nums.sort()
        ret=nums[-1]-nums[0]
        for i in range(4):
            ret=min(ret,nums[-(1+i)]-nums[3-i])
        return ret
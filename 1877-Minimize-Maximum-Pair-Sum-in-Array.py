class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ret=0
        for i in range(len(nums)//2):
            ret=max(ret,nums[i]+nums[len(nums)-1-i])
        return ret
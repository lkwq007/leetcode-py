class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                nums[j]=(nums[j]+nums[j+1])%10
        return nums[0]
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        acc=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                acc+=nums[i-1]+1-nums[i]
                nums[i]=nums[i-1]+1
        return acc
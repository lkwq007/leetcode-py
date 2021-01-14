class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Binary search
        left=0
        right=len(nums)-1
        while left<right:
            middle=left+(right-left)//2
            if nums[middle]>nums[middle+1]:
                right=middle
            else:
                left=middle+1
        return left

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left=nums[i]-1 if i==0 else nums[i-1]
            right=nums[i]-1 if i==len(nums)-1 else nums[i+1]
            if left<nums[i] and right<nums[i]:
                return i
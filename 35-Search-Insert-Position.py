class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>nums[-1]:
            return len(nums)
        left=0
        right=len(nums)-1
        while left<right:
            middle=left+(right-left)//2
            if nums[middle]==target:
                return middle
            if nums[middle]>target:
                right=middle
            else:
                left=middle+1
        return left
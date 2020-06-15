class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        left=0
        right=len(nums)-1
        while left<right:
            middle=left+(right-left)//2
            if middle%2==0 and nums[middle]==nums[middle+1] or middle%2==1 and nums[middle]==nums[middle-1]:
                left=middle+1
            else:
                right=middle
        return nums[left]
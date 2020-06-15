class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<1:
            return [-1,-1]
        total=len(nums)
        left=0
        right=total-1
        while left!=right:
            middle=left+(right-left)//2
            if nums[middle]>target:
                right=middle
            elif nums[middle]<target:
                left=middle+1
            else:
                right=middle
        if nums[left]!=target:
            return [-1,-1]
        lo=left
        right=total-1
        while left<right:
            middle=left+(right-left)//2
            if nums[middle]>target:
                right=middle
            elif nums[middle]<target:
                left=middle+1
            else:
                left=middle+1
        if left<total and nums[left]==target:
            left=left
        elif nums[left-1]==target:
            left=left-1
        return [lo,left]
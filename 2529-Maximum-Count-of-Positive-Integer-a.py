class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left=0
        right=len(nums)
        while left<right:
            middle=left+(right-left)//2
            if nums[middle]<=0:
                left=middle+1
            else:
                right=middle
        pos=len(nums)-left
        left=0
        right=len(nums)
        while left<right:
            middle=left+(right-left)//2
            if nums[middle]<0:
                left=middle+1
            else:
                right=middle
        return max(left,pos)
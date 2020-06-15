class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total=len(nums)
        idx=total-1
        start=idx
        while idx>0:
            if nums[idx-1]<nums[idx]:
                nums[idx-1],nums[start]=nums[start],nums[idx-1]
                return
            idx-=1
        nums.sort()
        return
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total=len(nums)
        idx=total-1
        start=idx
        for i in range(total-2,-1,-1):
            for j in range(i+1,total):
                if nums[j]<nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    nums[(j+1):]=sorted(nums[(j+1):])
                    return
        nums.sort()
        return
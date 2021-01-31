class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # simple
        total=len(nums)
        idx=total-1
        start=idx
        for i in range(total-1,-1,-1):
            for j in range(total-1,i,-1):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    nums[(i+1):]=sorted(nums[(i+1):])
                    return
        nums.sort()
        return
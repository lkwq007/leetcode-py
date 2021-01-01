class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            nums[i]=acc
        for i in range(len(nums)):
            if i==0 and nums[-1]-nums[i]==0:
                return i
            if i>0 and nums[i-1]==nums[-1]-nums[i]:
                return i
        return -1
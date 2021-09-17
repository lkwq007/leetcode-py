class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret=nums[-1]-nums[0]
        for i in range(k-1,len(nums)):
            ret=min(nums[i]-nums[i-k+1],ret)
        return ret
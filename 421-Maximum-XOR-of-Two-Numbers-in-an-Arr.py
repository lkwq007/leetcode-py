class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # TLE
        ret=0
        nums=list(set(nums))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ret=max(ret,nums[i]^nums[j])
        return ret
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ret=[0]*len(nums)
        max_val=nums[0]
        for i in range(len(nums)):
            max_val=max(max_val,nums[i])
            ret[i]=ret[i-1]+max_val+nums[i]
        return ret

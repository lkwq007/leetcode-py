class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        idx=0
        ret=0
        for i in range(len(nums)):
            if idx%2==0 and i+1<len(nums) and nums[i+1]==nums[i]:
                ret+=1
            else:
                idx+=1
        if (len(nums)-ret)%2:
            ret+=1
        return ret
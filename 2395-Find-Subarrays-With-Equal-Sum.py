class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        record={}
        for i in range(1,len(nums)):
            cur=nums[i]+nums[i-1]
            if cur in record:
                return True
            record[cur]=1
        return False
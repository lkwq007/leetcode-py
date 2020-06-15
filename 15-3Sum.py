class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        record={}
        record[-nums[0]]=1
        ret=set()
        for i in range(1,len(nums)):
            for j in range(i+1,len(nums)):
                tmp=nums[i]+nums[j]
                if tmp in record:
                    ret.add((-tmp,nums[i],nums[j]))
            record[-nums[i]]=1
        return list(ret)
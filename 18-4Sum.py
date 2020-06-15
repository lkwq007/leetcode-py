class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        nums.sort()
        record={}
        record[nums[0]]=1
        ret=set()
        for i in range(1,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    tmp=target-nums[k]-nums[j]-nums[i]
                    if tmp in record:
                        ret.add((tmp,nums[i],nums[j],nums[k]))
            record[nums[i]]=1
        return list(ret)
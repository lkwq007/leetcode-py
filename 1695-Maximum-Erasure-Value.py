class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ret=nums[0]
        record={nums[0]:0}
        left=0
        acc=ret
        for i in range(1,len(nums)):
            item=nums[i]
            if item in record:
                idx=record[item]
                while left<=idx:
                    del record[nums[left]]
                    acc-=nums[left]
                    left+=1
                record[item]=i
            else:
                record[item]=i
            acc+=item
            ret=max(acc,ret)
        return ret

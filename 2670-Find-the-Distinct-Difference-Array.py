class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        ret=[0]*len(nums)
        acc={}
        for i in range(len(nums)):
            item=nums[i]
            acc[item]=acc.get(item,0)+1
            record[item]-=1
            if record[item]==0:
                del record[item]
            ret[i]=len(acc)-len(record)
        return ret
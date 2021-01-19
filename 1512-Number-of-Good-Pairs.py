class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        record={}
        ret=0
        for item in nums:
            cnt=record.get(item,0)
            record[item]=cnt+1
            ret+=cnt
        return ret
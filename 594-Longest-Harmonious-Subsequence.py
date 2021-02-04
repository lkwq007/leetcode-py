class Solution:
    def findLHS(self, nums: List[int]) -> int:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        ret=0
        for k,v in record.items():
            if k-1 in record:
                ret=max(record[k]+record[k-1],ret)
            if k+1 in record:
                ret=max(record[k]+record[k+1],ret)
        return ret
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        record={}
        for item in nums:
            record[item]=1
        ret=-1
        for item in nums:
            if item>0 and -item in record:
                ret=max(ret,item)
        return ret

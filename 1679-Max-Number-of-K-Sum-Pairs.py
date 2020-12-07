class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        record={}
        ret=0
        for item in nums:
            rest=k-item
            if record.get(rest,0)>0:
                record[rest]=record[rest]-1
                ret+=1
            else:
                record[item]=record.get(item,0)+1
        return ret
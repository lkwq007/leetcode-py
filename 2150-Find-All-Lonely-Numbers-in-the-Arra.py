class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        ret=[]
        for k,v in record.items():
            if v==1 and (k-1) not in record and (k+1) not in record:
                ret.append(k)
        return ret
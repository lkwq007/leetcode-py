class Solution:
    def findLucky(self, arr: List[int]) -> int:
        record={}
        for item in arr:
            record[item]=record.get(item,0)+1
        ret=-1
        for key,val in record.items():
            if key==val:
                ret=max(ret,key)
        return ret
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        record={}
        for item in s:
            record[item]=record.get(item,0)+1
        ret=len(s)
        for item in t:
            if item in record and record[item]>0:
                ret-=1
                record[item]-=1
        return ret
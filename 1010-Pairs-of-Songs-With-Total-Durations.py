class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        record={}
        lst=[]
        for i in range(60,1000,60):
            lst.append(i)
        ret=0
        for t in time:
            for item in lst:
                ret+=record.get(item-t,0)
            record[t]=record.get(t,0)+1
        return ret

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        record={}
        ret=0
        for t in time:
            r=t%60
            rest=0 if r==0 else 60-r
            ret+=record.get(rest,0)
            record[r]=record.get(r,0)+1
        return ret
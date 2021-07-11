class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        record={}
        def probe(a,b):
            if b<0:
                return 0
            if a==b:
                return record[a]*a
            lst=[record[item]*item for item in range(a,b+1)]
            prev,cur=0,0
            for item in lst:
                prev,cur=max(cur,prev),max(cur,prev+item)
            return max(prev,cur)
        for item in nums:
            record[item]=record.get(item,0)+1
        ret=0
        last=-2
        acc=0
        for key in sorted(record.keys()):
            if key==last+1:
                acc+=1
            else:
                ret+=probe(last-acc,last)
                acc=0
            last=key
        ret+=probe(last-acc,last)
        return ret

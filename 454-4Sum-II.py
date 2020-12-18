class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # brute force
        record={}
        for a in A:
            for b in B:
                item=a+b
                record[item]=record.get(item,0)+1
        ret=0
        for c in C:
            for d in D:
                item=-c-d
                if item in record:
                    ret+=record[item]
        return ret

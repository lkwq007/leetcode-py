class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # brute force
        ret=0
        term=10**9+7
        record={}
        for item in deliciousness:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        for key in keys:
            mask=1
            for i in range(22):
                item=mask-key
                if item in record:
                    if item==key:
                        ret+=record[key]*(record[key]-1)//2
                    else:
                        ret+=record[key]*record[item]
                mask=mask<<1
            del record[key]
        return ret%term

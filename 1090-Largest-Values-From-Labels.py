class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        record={}
        lst=[i for i in range(len(values))]
        lst.sort(key=lambda x:-values[x])
        cnt=0
        acc=0
        for idx in lst:
            tmp=record.get(labels[idx],0)
            if tmp>=use_limit:
                continue
            acc+=values[idx]
            record[labels[idx]]=tmp+1
            cnt+=1
            if cnt==num_wanted or values[idx]==0:
                return acc
        return acc
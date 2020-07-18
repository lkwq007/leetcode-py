class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # answer is unique
        # better than o(nlogn)
        record={}
        max_val=0
        for item in nums:
            tmp=record.get(item,0)+1
            max_val=max(max_val,tmp)
            record[item]=tmp
        count=[[] for i in range(max_val+1)]
        for key,val in record.items():
            count[val].append(key)
        ret=[]
        cnt=0
        for i in range(max_val,-1,-1):
            ret.extend(count[i])
            cnt+=len(count[i])
            if cnt==k:
                return ret
        return ret

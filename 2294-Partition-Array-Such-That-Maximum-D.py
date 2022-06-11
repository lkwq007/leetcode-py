class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort()
        last=keys[0]
        ret=1
        for i in range(1,len(keys)):
            if last+k>=keys[i]:
                continue
            else:
                ret+=1
                last=keys[i]
        return ret
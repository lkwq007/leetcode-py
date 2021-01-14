class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort()
        for key in keys:
            for i in range(record[key]):
                cur=key
                while record.get(cur,0)>0:
                    record[cur]-=1
                    cur+=1
                if cur-key+1<3:
                    return False
        return True
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # a lazy way
        if len(nums)%k!=0:
            return False
        if k==1:
            return True
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort()
        for key in keys:
            cnt=record[key]
            if cnt>0:
                for i in range(key,key+k):
                    if record.get(i,0)>=cnt:
                        record[i]-=cnt
                    else:
                        return False
        return True
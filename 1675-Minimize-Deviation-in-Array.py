class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        record={}
        cnt=0
        for item in nums:
            if item&1:
                cnt+=1
                record[item]=1
        key=list(record.keys())
        key.sort()
        if cnt==len(nums):
            return key[-1]-key[0]
        elif cnt==0:
            return 0
        for item in nums:
            if item%2==0:
                while item>=key[-1] and :
                    
        ret=0
        for item in key:
            while True:
                if item*2>=key[-1]:
                    break
                item*=2
            ret=max(ret,key[-1]-item)
        return ret

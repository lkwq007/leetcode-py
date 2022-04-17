class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sliding window?
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        lst=[[key,val] for key,val in record.items()]
        lst.sort()
        ret=lst[0][1]
        cnt=ret
        acc=0
        left=0
        for i in range(1,len(lst)):
            acc=acc+(lst[i][0]-lst[i-1][0])*cnt
            cnt+=lst[i][1]
            if acc>k:
                while left<i and acc>k:
                    acc-=(lst[i][0]-lst[left][0])*lst[left][1]
                    cnt-=lst[left][1]
                    left+=1
                total=(k-acc)//(lst[i][0]-lst[left-1][0])
                if total>0:
                    left-=1
                    lst[left][1]=total
                    cnt+=total
                    acc+=total*(lst[i][0]-lst[left][0])
            ret=max(ret,cnt)
        return ret
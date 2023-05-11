class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        lst=sorted(record.keys())
        prefix=[0]*(len(lst)+1)
        for i in range(len(lst)):
            prefix[i]=prefix[i-1]+record[lst[i]]
        left=0
        right=len(lst)-1
        term=10**9+7
        ret=0
        while left<=right:
            cur=lst[left]
            if cur+cur>target:
                break
            while cur+lst[right]>target:
                right-=1
            total=prefix[right]-prefix[left]
            ret+=pow(2,total,term)*(pow(2,record[lst[left]],term)-1)
            ret%=term
            left+=1
        return ret

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        # brute force
        prefix=[0]*(len(nums)+1)
        for i in range(len(nums)):
            cur=1 if nums[i]%p==0 else 0
            prefix[i]=cur+prefix[i-1]
        ret=set([])
        for i in range(len(nums)):
            lst=[]
            for j in range(i,len(nums)):
                lst.append(nums[j])
                if prefix[j]-prefix[i-1]<=k:
                    ret.add(tuple(lst))
        return len(ret)
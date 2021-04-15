class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        lst=[]
        for i in range(len(nums)):
            acc=0
            for j in range(i,len(nums)):
                acc+=nums[j]
                lst.append(acc)
        lst.sort()
        idx=left-1
        ret=0
        term=10**9+7
        while idx<right:
            ret+=lst[idx]
            ret%=term
            idx+=1
        return ret
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total=sum(nums)
        if total<2:
            return 0
        prefix=[0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i]=nums[i]+prefix[i-1]
        ret=len(nums)
        for i in range(len(nums)):
            if i<total:
                rest=total-i-1
                cur=prefix[i]+prefix[len(nums)-1]-prefix[len(nums)-1-rest]
            else:
                cur=prefix[i]-prefix[i-total]
            ret=min(total-cur,ret)
        return ret

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_val=min(nums)
        max_val=max(nums)
        left=min_val
        right=max_val
        def check(x:int)->bool:
            acc=0
            prev=0
            for i in range(len(nums)):
                cur=1 if nums[i]<=x else 0
                acc,prev=max(acc,prev+cur),max(prev,acc)
            return max(acc,prev)>=k
        while left<right:
            middle=left+(right-left)//2
            if not check(middle):
                left=middle+1
            else:
                right=middle
        return left

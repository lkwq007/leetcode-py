class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left=0
        acc=0
        if sum(nums)<x:
            return -1
        ret=len(nums)+1
        right=len(nums)
        while left<len(nums):
            acc+=nums[left]
            if acc==x:
                total=len(nums)-right+left+1
                ret=min(total,ret)
            elif acc>x:
                break
            left+=1
        while right>=0:
            

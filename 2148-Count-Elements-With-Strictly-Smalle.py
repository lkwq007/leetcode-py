class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        left=1
        while left<len(nums) and nums[left]==nums[left-1]:
            left+=1
        right=len(nums)-2
        while right>=0 and nums[right]==nums[right+1]:
            right-=1
        return max(0,right-left+1)

class Solution:
    def countElements(self, nums: List[int]) -> int:
        x0=max(nums)
        x1=min(nums)
        cnt=len(nums)
        for item in nums:
            if item==x0 or item==x1:
                cnt-=1
        return cnt
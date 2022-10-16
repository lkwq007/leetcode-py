class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(val):
            left=0
            for i in range(len(nums)):
                cur=nums[i]-left
                if cur>val:
                    return False
                left=max(val-cur,0)
            return True
        left=0
        right=max(nums)
        while left<right:
            middle=left+(right-left)//2
            if not check(middle):
                left=middle+1
            else:
                right=middle
        return left

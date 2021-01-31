class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # prefix sum
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            nums[i]=acc
        left=-1
        right=0
        ret=len(nums)+1
        for i in range(len(nums)):
            leftmost=0 if left<0 else nums[left]
            while nums[i]-leftmost>=s:
                ret=min(i-left,ret)
                left+=1
                leftmost=nums[left]
        return ret if ret<=len(nums) else 0

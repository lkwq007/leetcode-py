class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        nums.sort(key=lambda x:-x)
        acc=0
        for idx in range(len(nums)):
            acc+=nums[idx]
            if acc>total-acc:
                return nums[:idx+1]
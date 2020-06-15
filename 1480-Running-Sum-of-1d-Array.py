class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc=0
        for idx in range(len(nums)):
            acc+=nums[idx]
            nums[idx]=acc
        return nums
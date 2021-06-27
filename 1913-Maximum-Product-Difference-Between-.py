class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # 1 <= nums[i] <= 10^4
        nums.sort()
        return nums[-1]*nums[-2]-nums[0]*nums[1]
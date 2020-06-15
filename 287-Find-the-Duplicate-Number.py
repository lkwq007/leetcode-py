from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        idx=0
        total=len(nums)
        while idx<total-1:
            if nums[idx]==nums[idx+1]:
                return nums[idx]
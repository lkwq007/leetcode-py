import re


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        # sum(nums)=2*sum(arr)
        # N^2?
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        nums.sort()
        
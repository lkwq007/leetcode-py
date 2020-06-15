class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=nums[0]
        for item in nums[1:]:
            result=item^result
        return result
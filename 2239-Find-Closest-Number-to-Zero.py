class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ret=nums[0]
        for item in nums:
            if abs(item)<abs(ret):
                ret=item
            elif abs(item)==abs(ret) and item>ret:
                ret=item
        return ret
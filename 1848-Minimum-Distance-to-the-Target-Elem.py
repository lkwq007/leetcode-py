class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        offset=0
        while start-offset>=0 or start+offset<len(nums):
            if start-offset>=0 and nums[start-offset]==target:
                return offset
            if start+offset<len(nums) and nums[start+offset]==target:
                return offset
            offset+=1
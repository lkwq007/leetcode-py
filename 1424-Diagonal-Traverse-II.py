class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if len(nums)<1 or len(nums[0])<1:
            return []
        height=len(nums)
        ret=[]
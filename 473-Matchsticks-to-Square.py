class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%4!=0:
            return False
        
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums)-sum(map(lambda x:sum(map(int,str(x))),nums)))
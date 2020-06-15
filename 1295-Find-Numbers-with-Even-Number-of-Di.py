class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        import functools
        return functools.reduce(lambda x,y: x+1-len(str(y))%2,nums,0)
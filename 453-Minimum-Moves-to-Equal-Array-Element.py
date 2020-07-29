class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        return total%n
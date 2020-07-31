class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        if total%n==0:
            return n
        return total%n
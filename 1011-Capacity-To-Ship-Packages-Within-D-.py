class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        dp=[[0]*len(weights) for _ in range(days)]
        
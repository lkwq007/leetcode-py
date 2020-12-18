class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # H>=len(piles)
        if H==len(piles):
            return max(piles)
        
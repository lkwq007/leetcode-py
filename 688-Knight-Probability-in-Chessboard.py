class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K<1:
            return 1.0
        if r-2*K>=0 and r+2*K<N and c-2*K>=0 and c+2*K<N:
            return 1.0
        
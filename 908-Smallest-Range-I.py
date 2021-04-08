class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_val=min(A)
        max_val=max(A)
        if min_val+K+K<max_val:
            return max_val-min_val-K-K
        return 0
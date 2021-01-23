class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if n<2:
            return 0
        record={}
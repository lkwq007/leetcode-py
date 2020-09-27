class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        w=len(grid[0])
        if k%w==0:
            return grid
        
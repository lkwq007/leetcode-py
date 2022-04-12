class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        h=len(grid)
        w=len(grid[0])
        total=h*w
        return [[grid[(i*w+j-k+total)%total//w][(i*w+j-k+total)%total%w] for j in range(len(grid[0]))] for i in range(len(grid))]        
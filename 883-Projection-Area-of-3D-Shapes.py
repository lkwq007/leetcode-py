class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        ret=0
        for y in range(n):
            acc0=0
            acc1=0
            for x in range(n):
                if grid[y][x]>0:
                    ret+=1
                acc0=max(acc0,grid[y][x])
                acc1=max(acc1,grid[x][y])
            ret+=acc0+acc1
        return ret
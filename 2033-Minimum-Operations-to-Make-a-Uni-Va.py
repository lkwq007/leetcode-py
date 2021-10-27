class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        minval=grid[0][0]
        maxval=grid[0][0]
        h=len(grid)
        w=len(grid[0])
        for y in range(h):
            for x in range(w):
                item=grid[y][x]
                maxval=max(maxval,item)
                minval=min(minval,item)
        if (maxval-minval)%x!=0:
            return -1
        
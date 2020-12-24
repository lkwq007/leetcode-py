class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # only 2D grid
        h=len(grid)
        w=len(grid[0])
        overlap=0
        ret=0
        for y in range(h):
            for x in range(w):
                item=grid[y][x]
                if item>0:
                    ret+=2+item*4
                if x+1<w:
                    overlap+=2*min(item,grid[y][x+1])
                if y+1<h:
                    overlap+=2*min(item,grid[y+1][x])
        return ret-overlap
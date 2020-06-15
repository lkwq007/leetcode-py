class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if len(grid)<1 or len(grid[0])<1:
            return 0
        height=len(grid)
        width=len(grid[0])
        max_top=[0]*width
        max_left=[0]*height
        for y in range(0,height):
            for x in range(0,width):
                max_top[x]=max(max_top[x],grid[y][x])
                max_left[y]=max(max_left[y],grid[y][x])
        acc=0
        for y in range(0,height):
            for x in range(0,width):
                acc+=min(max_top[x],max_left[y])-grid[y][x]
        return acc
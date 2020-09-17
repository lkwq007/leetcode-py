class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n=len(grid)
        total=0
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(y0,x0):
            
        for y in range(n):
            for x in range(n):
                if grid[y][x][0]!="2":
                    dfs(y,x)
                    total+=1
        return total
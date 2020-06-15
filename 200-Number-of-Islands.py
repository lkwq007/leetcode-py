class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)<1:
            return 0
        if len(grid[0])<1:
            return 0
        h=len(grid)
        w=len(grid[0])
        def dfs(y,x,cnt):
            if grid[y][x]=="1":
                grid[y][x]=cnt
            else:
                return
            up=y-1 if y>0 else y
            down=y+1 if y<h else y
            if x>0 and grid[y][x-1]=="1":
                dfs(y,x-1,cnt)
            if x<w-1 and grid[y][x+1]=="1":
                dfs(y,x+1,cnt)
            if y>0 and grid[y-1][x]=="1":
                dfs(y-1,x,cnt)
            if y<h-1 and grid[y+1][x]=="1":
                dfs(y+1,x,cnt)
        total=0
        for y in range(0,h):
            for x in range(0,w):
                if grid[y][x]=="1":
                    dfs(y,x,2)
                    total+=1
                else:
                    continue
        return total
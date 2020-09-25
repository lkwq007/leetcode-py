class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n=len(grid)
        template=[0]*n
        visited=[template[:] for _ in range(n)]
        total=0
        upper=1
        bottom=2
        cell=3
        direction=[
            [(1,0),(-1,0),(0,1),(0,-1)],
            [(-1,0),(0,-1)],
            [(1,0),(0,1)],
            [(-1,0),(0,1)],
            [(1,0),(0,-1)]
        ]
        def possible_direction(y,x,part):
            if grid[y][x]==" ":
                return direction[0]
            elif grid[y][x]=="/":
                return direction[1+(0 if part==upper else 1)]
            else:
                return direction[3+(0 if part==upper else 1)]
        def dfs(y0,x0,part):
            if visited[y0][x0]&part!=0:
                return
            if grid[y0][x0]==" ":
                visited[y0][x0]=cell
            else:
                visited[y0][x0]|=part
            for y_offset,x_offset in possible_direction(y0,x0,part):
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<n and 0<=x1<n:
                    if x_offset==0:
                        dfs(y1,x1,upper if y_offset>0 else bottom)
                    elif x_offset>0:
                        dfs(y1,x1,upper if grid[y1][x1]=="/" else bottom)
                    else:
                        dfs(y1,x1,bottom if grid[y1][x1]=="/" else upper)
        for y in range(n):
            for x in range(n):
                if visited[y][x]&upper==0:
                    dfs(y,x,upper)
                    total+=1
                if visited[y][x]&bottom==0:
                    dfs(y,x,bottom)
                    total+=1
        return total
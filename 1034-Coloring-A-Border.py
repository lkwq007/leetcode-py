class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        current=grid[r0][c0]
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        h=len(grid)
        w=len(grid[0])
        border=[]
        def dfs(y,x):
            cnt=0
            grid[y][x]=-1
            queue=[]
            for y_offset,x_offset in direction:
                y1=y+y_offset
                x1=x+x_offset
                if 0<=y1<h and 0<=x1<w:
                    if grid[y1][x1]==current:
                        dfs(y1,x1)
                        cnt+=1
                    elif grid[y1][x1]<0:
                        cnt+=1
            if cnt<4:
                border.append((y,x))
            grid[y][x]=current
        dfs(r0,c0)
        for y,x in border:
            grid[y][x]=color
        return grid

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        current=grid[r0][c0]
        if color==current:
            return grid
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        h=len(grid)
        w=len(grid[0])
        def dfs(y,x):
            if y<0 or x<0 or y>=h or x>=w or abs(grid[y][x])!=current:
                return 0
            if grid[y][x]==-current:
                return 1
            grid[y][x]=-current
            cnt=0
            for y_offset,x_offset in direction:
                y1=y+y_offset
                x1=x+x_offset
                cnt+=dfs(y1,x1)
            if cnt==4:
                grid[y][x]=current
            return 1
        dfs(r0,c0)
        for y in range(h):
            for x in range(w):
                if grid[y][x]<0:
                    grid[y][x]=color
        return grid

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        current=grid[r0][c0]
        if color==current:
            return grid
        visited=set([])
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        h=len(grid)
        w=len(grid[0])
        def dfs(y,x):
            # should check visited first
            if (y,x) in visited:
                return 1
            if y<0 or x<0 or y>=h or x>=w or grid[y][x]!=current:
                return 0
            visited.add((y,x))
            cnt=0
            for y_offset,x_offset in direction:
                y1=y+y_offset
                x1=x+x_offset
                cnt+=dfs(y1,x1)
            if cnt<4:
                grid[y][x]=color
            return 1
        dfs(r0,c0)
        return grid
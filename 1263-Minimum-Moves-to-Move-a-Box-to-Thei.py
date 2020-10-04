class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        h=len(grid)
        w=len(grid[0])
        for y in range(h):
            for x in range(w):
                if grid[y][x]=="S":
                    player=(y,x)
                elif grid[y][x]=="B":
                    box=(y,x)
        # first check
        template=[-1]*w
        visited=[template[:] for _ in range(h)]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(y0,x0,target):
            tmp=visited[y0][x0]
            visited[y0][x0]=-2
            flag=False
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w and grid[y1][x1]!="#":
                    if grid[y1][x1]==target:
                        flag=True
                        break
                    elif visited[y1][x1]!=-2:
                        if dfs(y1,x1,target):
                            flag=True
                            break
            visited[y0][x0]=tmp
            return flag
        if not (dfs(player[0],player[1],"B") and dfs(box[0],box[1],"T")):
            return -1
        visited[box[0]][box[1]]=0
        step=0
        queue=[box]
        while queue:
            target=[]
            for y0,x0 in queue:
                
        return -1

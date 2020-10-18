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
        tin=[template[:] for _ in range(h)]
        low=[template[:] for _ in range(h)]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        last=[]
        def check(y0,x0,target):
            tmp=visited[y0][x0]
            visited[y0][x0]=-2
            flag=False
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w and grid[y1][x1]!="#":
                    if grid[y1][x1]==target:
                        last.append((y0,x0))
                        flag=True
                        break
                    elif visited[y1][x1]!=-2 and check(y1,x1,target):
                        flag=True
                        break
            visited[y0][x0]=tmp
            return flag
        if not (check(player[0],player[1],"B") and check(box[0],box[1],"T")):
            return -1
        articulation={}
        self.timer=1
        def dfs(y0,x0,yp,xp):
            tin[y0][x0]=self.timer
            low[y0][x0]=self.timer
            self.timer+=1
            cnt=0
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w and grid[y1][x1]!="#":
                    if yp==y1 and xp==x1:
                        continue
                    elif tin[y1][x1]!=-1:
                        low[y0][x0]=min(low[y0][x0],tin[y1][x1])
                    else:
                        cnt+=1
                        dfs(y1,x1,y0,x0)
                        low[y0][x0]=min(low[y0][x0],low[y1][x1])
                        if low[y1][x1]>=tin[y1][x1] and yp!=-1:
                            articulation[(y0,x0)]=1
            if yp==-1 and cnt>1:
                articulation[(y0,x0)]=1
        for y in range(h):
            for x in range(w):
                if tin[y][x]==-1:
                    dfs(y,x,-1,-1)
        queue=[(*box,*(last[0]))]
        visited[box[0]][box[1]]=0
        step=0
        while queue:
            target=[]
            step+=1
            for y0,x0,ys,xs in queue:
                
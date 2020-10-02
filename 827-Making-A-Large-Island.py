class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ret=1
        size=[]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        h=len(grid)
        w=len(grid[0])
        def dfs(y0,x0,mark):
            if grid[y0][x0]==1:
                grid[y0][x0]=mark
            inc=0
            cnt=0 
            seen=[]
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=x1<w and 0<=y1<h:
                    if grid[y0][x0]==0 and grid[y1][x1]<0 and grid[y1][x1]!=mark and grid[y1][x1] not in seen:
                        seen.append(grid[y1][x1])
                        inc+=size[-grid[y1][x1]-1]
                    elif grid[y0][x0]==mark and grid[y1][x1]>=0:
                        a,b=dfs(y1,x1,mark)
                        cnt+=a
                        inc=max(inc,b)
            return cnt+(0 if grid[y0][x0]==0 else 1),inc+(1 if grid[y0][x0]==0 else 0)
        idx=-1
        for y in range(h):
            for x in range(w):
                if grid[y][x]==1:
                    cnt,inc=dfs(y,x,idx)
                    size.append(cnt)
                    ret=max(ret,cnt+inc)
                    idx-=1
        return ret

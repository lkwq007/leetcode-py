class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        total=sum(map(sum,grid))
        h=len(grid)
        w=len(grid[0])
        if total==0 or total==h*w:
            return -1
        queue=[]
        for y in range(h):
            for x in range(w):
                if grid[y][x]==1:
                    queue.append((y,x))
                else:
                    grid[y][x]=-(h+w)
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        ret=0
        while queue:
            target=[]
            record={}
            for y0,x0 in queue:
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    tmp=grid[y0][x0]
                    ret=min(ret,tmp)
                    if 0<=y1<h and 0<=x1<w and grid[y1][x1]!=1:
                        if tmp-1>grid[y1][x1]:
                            grid[y1][x1]=tmp-1
                            if (y1,x1) not in record:
                                record[(y1,x1)]=1
                                target.append((y1,x1))
                        ret=min(ret,grid[y1][x1])
            queue=target
        return -ret+1

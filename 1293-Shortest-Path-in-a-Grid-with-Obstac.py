class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue=[(0,0,k)]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        h=len(grid)
        w=len(grid[0])
        step=0
        if h==1 and w==1:
            return 0
        visited={}
        while queue:
            target={}
            step+=1
            for y0,x0,r in queue:
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    if 0<=y1<h and 0<=x1<w:
                        if y1==h-1 and x1==w-1:
                            return step
                        if (y1,x1) in visited:
                            if visited[(y1,x1)]>=r:
                                continue
                        if grid[y1][x1]==0:
                            visited[(y1,x1)]=r
                            target[(y1,x1)]=max(target.get((y1,x1),r),r)
                        else:
                            if r>0:
                                visited[(y1,x1)]=r-1
                                target[(y1,x1)]=max(target.get((y1,x1),r-1),r-1)
            queue=[(k[0],k[1],v) for k,v in target.items()]
        return -1

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        h=len(grid)
        w=len(grid[0])
        cnt=sum(grid[0])
        for y in range(1,h):
            cnt+=grid[y][w-1]
        # if we can directly go to dest
        if k>=cnt:
            return h+w-2
        queue=[(0,0,k)]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        step=0
        template=[-1]*w
        visited=[template[:] for _ in range(h)]
        while queue:
            target={}
            step+=1
            for y0,x0,r in queue:
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    if 0<=y1<h and 0<=x1<w:
                        if y1==h-1 and x1==w-1:
                            return step
                        if visited[y1][x1]>=r:
                            continue
                        if grid[y1][x1]==0:
                            visited[y1][x1]=r
                            target[(y1,x1)]=max(target.get((y1,x1),r),r)
                        else:
                            if r>0:
                                visited[y1][x1]=r-1
                                target[(y1,x1)]=max(target.get((y1,x1),r-1),r-1)
            queue=[(k[0],k[1],v) for k,v in target.items()]
        return -1
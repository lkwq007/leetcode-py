class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid)<1 or len(grid[0])<1:
            return 0
        h=len(grid)
        w=len(grid[0])
        cnt=0
        for y in range(h):
            for x in range(w):
                if grid[y][x]:
                    if x>0 and grid[y][x-1]:
                        cnt-=2
                    if y>0 and grid[y-1][x]:
                        cnt-=2
                    cnt+=4
        return cnt

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid)<1 or len(grid[0])<1:
            return 0
        counter=[0]*5
        h=len(grid)
        w=len(grid[0])
        direction=[[-1,0],[1,0],[0,-1],[0,1]]
        for y in range(h):
            for x in range(w):
                if grid[y][x]:
                    cnt=0
                    for y_offset,x_offset in direction:
                        y_new=y+y_offset
                        x_new=x+x_offset
                        if 0<=y_new<h and 0<=x_new<w and grid[y_new][x_new]:
                            cnt+=1
                    counter[cnt]+=1
        ret=0
        for i in range(0,5):
            ret+=i*counter[~i]
        return ret

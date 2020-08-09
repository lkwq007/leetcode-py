# a BFS for rotten orange could also work fine
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h=len(grid)
        w=len(grid[0])
        queue=[]
        for y in range(h):
            for x in range(w):
                if grid[y][x]==1:
                    queue.append((y,x))
        minute=0
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            target=[]
            rotten=[]
            for y,x in queue:
                cnt=0
                for y_offset,x_offset in direction:
                    y_next=y+y_offset
                    x_next=x+x_offset
                    if 0<=y_next<h and 0<=x_next<w and grid[y_next][x_next]==2:
                        cnt+=1
                        break
                if cnt==0:
                    target.append((y,x))
                else:
                    rotten.append((y,x))
            for y,x in rotten:
                grid[y][x]=2
            if len(rotten)==0:
                return -1
            queue=target
            minute+=1
        return minute
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        if len(grid)<2 and len(grid[0])<2:
            return 1
        queue=[(0,0)]
        target=[]
        ret=1
        h=len(grid)
        w=len(grid[0])
        while True:
            for idx in range(len(queue)):
                y,x=queue[idx]
                grid[y][x]=-ret
                for y_next in range(y-1,y+2):
                    for x_next in range(x-1,x+2):
                        if y_next<0 or y_next>=h or x_next<0 or x_next>=w:
                            continue
                        if grid[y_next][x_next]==0:
                            grid[y_next][x_next]=-ret-1
                            target.append((y_next,x_next))
                        if y_next==h-1 and x_next==w-1:
                            return ret+1
            if len(target)<1:
                return -1
            ret+=1
            queue=target
            target=[]
        return -1
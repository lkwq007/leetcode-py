class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # bfs
        record={}
        queue=[(i,0) for i in range(len(grid))]
        ret=0
        while queue:
            target=[]
            for y,x in queue:
                ret=max(ret,x)
                if x==len(grid[0])-1:
                    return x
                for next in range(max(0,y-1),min(len(grid),y+2)):
                    if grid[y][x]<grid[next][x+1] and (next,x+1) not in record:
                        record[(next,x+1)]=1
                        target.append((next,x+1))

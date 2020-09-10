class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        mapping={"R":(0,1),"L":(0,-1),"D":(1,0),"U":(-1,0)}
        reverted={"L":"R","R":"L","U":"D","D":"U"}
        streets=["","LR","UD","LD","RD","UL","UR"]
        h=len(grid)
        w=len(grid[0])
        def dfs(y0,x0):
            if y0==h-1 and x0==w-1:
                return True
            print(y0,x0)
            cur=grid[y0][x0]
            street=streets[cur]
            grid[y0][x0]=0
            for direction in street:
                y_offset,x_offset=mapping[direction]
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=x1<w and 0<=y1<h and grid[y1][x1]>0:
                    next=grid[y1][x1]
                    if reverted[direction] in streets[next]:
                        if dfs(y1,x1):
                            return True
            return False
        return dfs(0,0)

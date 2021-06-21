# one dfs is enough, only need to dfs grid2 and check grid1
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # two dfs
        offset=[[1,0],[0,1],[-1,0],[0,-1]]
        h=len(grid1)
        w=len(grid1[0])
        def dfs(y,x,mark):
            grid1[y][x]=mark
            for yo,xo in offset:
                yn=y+yo
                xn=x+xo
                if 0<=yn<h and 0<=xn<w and grid1[yn][xn]==1:
                    dfs(yn,xn,mark)
        acc=2
        for y in range(h):
            for x in range(w):
                if grid1[y][x]==1:
                    dfs(y,x,acc)
                    acc+=1
        def check(y,x,mark):
            grid2[y][x]=0
            ret=True
            if grid1[y][x]!=mark:
                ret=False
            for yo,xo in offset:
                yn=y+yo
                xn=x+xo
                if 0<=yn<h and 0<=xn<w and grid2[yn][xn]==1:
                    # note that it cannot be `ret and check()`
                    ret=check(yn,xn,mark) and ret
            return ret
        cnt=0
        for y in range(h):
            for x in range(w):
                if grid2[y][x]==1:
                    if check(y,x,grid1[y][x]) and grid1[y][x]>0:
                        cnt+=1
        return cnt
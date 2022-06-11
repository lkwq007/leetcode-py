class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        term=10**9+7
        h=len(grid)
        w=len(grid[0])
        neg=[[1]*(w+1) for _ in range(h+1)]
        pos=[[-1]*(w+1) for _ in range(h+1)]
        if grid[0][0]==0:
            return 0
        elif grid[0][0]>0:
            pos[0][0]=grid[0][0]
        else:
            neg[0][0]=grid[0][0]
        for y in range(h):
            for x in range(w):
                if y==0 and x==0:
                    continue
                cur=grid[y][x]
                if cur==0:
                    pos[y][x]=0
                    neg[y][x]=0
                elif cur>0:
                    pos[y][x]=cur*max(pos[y-1][x],pos[y][x-1])
                    neg[y][x]=cur*min(neg[y-1][x],neg[y][x-1])
                else:
                    neg[y][x]=cur*max(pos[y-1][x],pos[y][x-1])
                    pos[y][x]=cur*min(neg[y-1][x],neg[y][x-1])
        if pos[-2][-2]>=0:
            return pos[-2][-2]%term
        return -1

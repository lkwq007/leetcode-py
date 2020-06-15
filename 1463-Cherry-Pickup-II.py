class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if len(grid)<1 or len(grid[0])<1:
            return 0
        h=len(grid)
        w=len(grid[0])
        template=[0]*(w+1)
        dp=[template[:] for _ in range(w+1)]
        dp_last=[template[:] for _ in range(w+1)]
        dp_last[0][w-1]=grid[0][-1]+grid[0][0]
        offset=[-1,0,1]
        for y in range(1,h):
            left=min(y+1,w)
            right=w-left-1
            for i in range(0,left):
                for j in range(w-1,right,-1):
                    if i==j:
                        cur=grid[y][i]
                    else:
                        cur=grid[y][i]+grid[y][j]
                    max_val=0
                    for i_offset in offset:
                        for j_offset in offset:
                            max_val=max(max_val,dp_last[i+i_offset][j+j_offset])
                    dp[i][j]=cur+max_val
            tmp=dp_last
            dp_last=dp
            dp=tmp
        ret=0
        for i in range(0,w):
            for j in range(0,w):
                ret=max(ret,dp_last[i][j])
        return ret

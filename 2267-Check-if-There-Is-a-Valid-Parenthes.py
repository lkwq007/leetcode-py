class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0]==")":
            return False
        h=len(grid)
        w=len(grid[0])
        template=[0]*w
        dp=[template[:] for _ in range(h)]
        dp[0][0]=[1]
        for x in range(1,w):
            val=1 if grid[0][x]=="(" else -1
            record=set([])
            for prev in dp[0][x-1]:
                cur=prev+val
                if cur>=0:
                    record.add(cur)
            dp[0][x]=record
        for y in range(1,h):
            for x in range(w):
                val=1 if grid[y][x]=="(" else -1
                record=set([])
                if x>0:
                    for prev in dp[y][x-1]:
                        cur=prev+val
                        if cur>=0:
                            record.add(cur)
                for prev in dp[y-1][x]:
                    cur=prev+val
                    if cur>=0:
                        record.add(cur)
                dp[y][x]=record
        return 0 in dp[-1][-1]
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        h=len(grid)
        w=len(grid[0])
        dp=[[h*w+1]*w for _ in range(h)]
        dp[0][0]=0
        offset=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=deque([(0,0)])
        while queue:
            y,x=queue.popleft()
            if (y,x)==(h-1,w-1):
                return dp[y][x]
            for i in range(len(offset)):
                yo,xo=offset[i]
                yn=y+yo
                xn=x+xo
                dist=0 if grid[y][x]-1==i else 1
                if 0<=yn<h and 0<=xn<w and dp[y][x]+dist<dp[yn][xn]:
                    dp[yn][xn]=dp[y][x]+dist
                    if grid[y][x]-1==i:
                        queue.appendleft((yn,xn))
                    else:
                        queue.append((yn,xn))
            # [print(item) for item in dp]
            # print(queue)
        return dp[-1][-1]

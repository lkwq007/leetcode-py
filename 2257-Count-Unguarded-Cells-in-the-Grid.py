class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        template=[0]*n
        grid=[template[:] for _ in range(m)]
        for y,x in walls:
            grid[y][x]=3
        for y,x in guards:
            grid[y][x]=3
        queue=[(y,x,0) for y,x in guards]+[(y,x,1) for y,x in guards]
        while queue:
            target=[]
            for y,x,t in queue:
                if t==0:
                    xn=x
                    for yn in [y-1,y+1]:
                        if 0<=xn<n and 0<=yn<m and grid[yn][xn]&1==0:
                            grid[yn][xn]=grid[yn][xn]|1
                            target.append((yn,xn,t))
                else:
                    yn=y
                    for xn in [x-1,x+1]:
                        if 0<=xn<n and 0<=yn<m and grid[yn][xn]&2==0:
                            grid[yn][xn]=grid[yn][xn]|2
                            target.append((yn,xn,t))
            queue=target
        ret=0
        for y in range(m):
            for x in range(n):
                if grid[y][x]==0:
                    ret+=1
        return ret
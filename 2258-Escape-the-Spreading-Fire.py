class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        inf=2*10**9
        queue=[]
        h=len(grid)
        w=len(grid[0])
        for y in range(h):
            for x in range(w):
                if grid[y][x]==1:
                    queue.append((y,x))
        template=[inf]*w
        state=[template[:] for _ in range(h)]
        step=1
        for y,x in queue:
            state[y][x]=0
        offset=[(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            target=[]
            for y,x in queue:
                for yo,xo in offset:
                    yn=y+yo
                    xn=x+xo
                    if 0<=xn<w and 0<=yn<h and state[yn][xn]==inf and grid[yn][xn]!=2:
                        state[yn][xn]=step
                        target.append((yn,xn))
            queue=target
            step+=1
        # [print(item) for item in state]
        # finding path which min-state is max
        queue=[(0,0,state[0][0]-1)]
        record={}
        record[(0,0)]=state[0][0]-1
        step=1
        while queue:
            target=[]
            for y,x,t in queue:
                for yo,xo in offset:
                    yn=y+yo
                    xn=x+xo
                    if 0<=xn<w and 0<=yn<h and grid[yn][xn]==0:
                        if xn==w-1 and yn==h-1:
                            cur=min(t,state[yn][xn]-step)
                        else:
                            cur=min(t,state[yn][xn]-step-1)
                        if (yn,xn) not in record or record[(yn,xn)]<cur:
                            record[(yn,xn)]=cur
                            target.append((yn,xn,cur))
            step+=1
            queue=target
        return max(min(record.get((h-1,w-1),-1),10**9),-1)

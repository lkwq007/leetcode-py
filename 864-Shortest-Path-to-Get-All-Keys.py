class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        key_num=0
        h=len(grid)
        w=len(grid[0])
        start=None
        for y in range(h):
            for x in range(w):
                if grid[y][x]=="@":
                    start=(y,x)
                if grid[y][x].isalpha():
                    key_num=max(key_num,ord(grid[y][x].lower())-ord("a")+1)
        if key_num==0 or start==None:
            return -1
        queue=[(start[0],start[1],0)]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        step=0
        mask=1
        mapping={".":0,"@":0}
        visited=[[{} for x in range(w)] for y in range(h)]
        visited[start[0]][start[1]][0]=0
        for i in range(key_num):
            mapping[chr(ord("a")+i)]=mask
            mapping[chr(ord("A")+i)]=mask
            mask=mask<<1
        full=mask-1
        while queue:
            target=[]
            step+=1
            for y0,x0,state in queue:
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    if 0<=y1<h and 0<=x1<w and grid[y1][x1]!="#":
                        val=grid[y1][x1]
                        mask=mapping[val]
                        if val.isupper() and mask&state:
                            if state not in visited[y1][x1]:
                                target.append((y1,x1,state))
                                visited[y1][x1][state]=step
                        elif val.islower():
                            if state|mask not in visited[y1][x1]:
                                target.append((y1,x1,state|mask))
                                visited[y1][x1][state|mask]=step
                            if mask|state==full:
                                return step
                        elif val=="." or val=="@":
                            if state not in visited[y1][x1]:
                                target.append((y1,x1,state))
                                visited[y1][x1][state]=step
            queue=target
        return -1
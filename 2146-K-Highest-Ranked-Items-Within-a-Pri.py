class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        record={}
        queue=[start]
        step=0
        offset=[(0,1),(1,0),(0,-1),(-1,0)]
        h=len(grid)
        w=len(grid[0])
        record[tuple(start)]=0
        while queue:
            target=[]
            step+=1
            for y,x in queue:
                for yo,xo in offset:
                    yn=y+yo
                    xn=x+xo
                    if 0<=yn<h and 0<=xn<w and (yn,xn) not in record and grid[yn][xn]!=0:
                        record[(yn,xn)]=step
                        target.append((yn,xn))
            queue=target
            step+=1
        ret=[]
        for key,_ in record.items():
            y,x=key
            if pricing[0]<=grid[y][x]<=pricing[1]:
                ret.append(key)
        ret.sort(key=lambda x:(record[x],grid[x[0]][x[1]],x[0],x[1]))
        return ret[:k]
                        


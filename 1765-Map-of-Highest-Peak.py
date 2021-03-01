class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # at least one water cell
        queue=[]
        h=len(isWater)
        w=len(isWater[0])
        for y in range(h):
            for x in range(w):
                if isWater[y][x]==1:
                    queue.append((y,x))
                    isWater[y][x]=0
                else:
                    isWater[y][x]=-1
        ret=isWater
        step=0
        target=[]
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        while queue:
            for y,x in queue:
                ret[y][x]=step
                for y_offset,x_offset in direction:
                    y1=y+y_offset
                    x1=x+x_offset
                    if 0<=y1<h and 0<=x1<w and ret[y1][x1]<0:
                        ret[y1][x1]=0
                        target.append((y1,x1))
            queue=target
            target=[]
            step+=1
        return ret
                
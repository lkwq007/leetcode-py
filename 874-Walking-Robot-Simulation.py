class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        grid={}
        for x,y in obstacles:
            grid[(x,y)]=1
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        idx=0
        y=0
        x=0
        ret=0
        for item in commands:
            if item==-1:
                idx+=1
                idx%=4
            elif item==-2:
                idx+=3
                idx%=4
            else:
                for step in range(1,item+1):
                    y_next=y+direction[idx][1]
                    x_next=x+direction[idx][0]
                    if (x_next,y_next) in grid:
                        break
                    y=y_next
                    x=x_next
                ret=max(ret,y*y+x*x)
        return ret

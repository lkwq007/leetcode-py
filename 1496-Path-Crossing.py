class Solution:
    def isPathCrossing(self, path: str) -> bool:
        y=0
        x=0
        mapping={
            "N":(0,1),"S":(0,-1),"E":(1,0),"W":(-1,0)
        }
        record={}
        record[(0,0)]=0
        for item in path:
            x1,y1=mapping[item]
            y+=y1
            x+=x1
            if (x,y) in record:
                return True
            record[(x,y)]=0
        return False
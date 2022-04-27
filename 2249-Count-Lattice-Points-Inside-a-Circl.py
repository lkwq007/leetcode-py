class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        record={}
        for x,y,r in circles:
            r2=r*r
            for i in range(x-r,x+r+1):
                for j in range(y-r,y+r+1):
                    if (i-x)*(i-x)+(j-y)*(j-y)<=r2:
                        record[(i,j)]=1
        return len(record)

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ret=[]
        h=len(land)
        w=len(land[0])
        for y in range(h):
            for x in range(w):
                if land[y][x]==1:
                    r=y
                    c=x
                    while r<h and land[r][c]==1:
                        r+=1
                    r-=1
                    while c<w and land[r][c]==1:
                        c+=1
                    c-=1
                    ret.append([y,x,r,c])
                    for i in range(y,r+1):
                        for j in range(x,c+1):
                            land[i][j]=0
        return ret
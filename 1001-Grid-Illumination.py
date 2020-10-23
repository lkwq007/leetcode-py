class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # sparse grid
        ret=[0]*len(queries)
        grid={}
        row={}
        col={}
        diag={}
        rdiag={}
        for y,x in lamps:
            row[y]=row.get(y,0)+1
            col[x]=col.get(x,0)+1
            grid[(y,x)]=1
            diag[y-x]=diag.get(y-x,0)+1
            rdiag[y+x-N]=diag.get(y+x-N,0)+1
        for i in range(len(queries)):
            y,x=queries[i]
            if row.get(y,0)>0 or col.get(x,0)>0 or diag.get(y-x,0) or rdiag.get(y+x-N,0)>0:
                ret[i]=1
            for y1 in range(y-1,y+2):
                for x1 in range(x-1,x+2):
                    if 0<=y1<N and 0<=x1<N:
                        if (y1,x1) in grid:
                            del grid[(y1,x1)]
                            row[y1]-=1
                            col[x1]-=1
                            diag[y1-x1]-=1
                            rdiag[y1+x1-N]-=1
        return ret
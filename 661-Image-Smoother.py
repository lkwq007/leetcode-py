class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if len(M)<1 or len(M[0])<1:
            return M
        h=len(M)
        w=len(M[0])
        # brute force
        def conv(y0,x0):
            cnt=0
            acc=0
            for y in range(y0-1,y0+2):
                for x in range(x0-1,x0+2):
                    if 0<=y<h and 0<=x<w:
                        acc+=M[y][x]
                        cnt+=1
            return acc//cnt
        template=[0]*w
        ret=[template[:] for _ in range(h)]
        for y in range(h):
            for x in range(w):
                ret[y][x]=conv(y,x)
        return ret

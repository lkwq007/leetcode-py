class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        h=len(A)
        w=len(A[0])
        queue=[]
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        record={}
        def dfs(y0,x0):
            A[y0][x0]=-1
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w:
                    if A[y1][x1]==1:
                        dfs(y1,x1)
                    elif A[y1][x1]==0:
                        # queue.append([y1][x1])
                        record[(y1,x1)]=1
        flag=False
        for y in range(h):
            for x in range(w):
                if A[y][x]==1:
                    dfs(y,x)
                    flag=True
                    break
            if flag:
                break
        target={}
        cnt=1
        while record:
            cnt+=1
            for y,x in record.keys():
                if A[y][x]==0:
                    A[y][x]=cnt
                    for y_offset,x_offset in direction:
                        y_next=y+y_offset
                        x_next=x+x_offset
                        if 0<=y_next<h and 0<=x_next<w:
                            if A[y_next][x_next]==0 and (y_next,x_next) not in record:
                                target[(y_next,x_next)]=1
                            elif A[y_next][x_next]==1:
                                return cnt-1
            record=target
            target={}
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        h=len(A)
        w=len(A[0])
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(y0,x0):
            A[y0][x0]=-1
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w and A[y1][x1]==1:
                    dfs(y1,x1)
        for y in range(h):
            if A[y][0]==1:
                dfs(y,0)
            if A[y][w-1]==1:
                dfs(y,w-1)
        for x in range(w):
            if A[0][x]==1:
                dfs(0,x)
            if A[h-1][x]==1:
                dfs(h-1,x)
        ret=0
        for y in range(h):
            for x in range(w):
                if A[y][x]==1:
                    ret+=1
        return ret


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        h=len(A)
        w=len(A[0])
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(y0,x0):
            A[y0][x0]=0
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w and A[y1][x1]==1:
                    dfs(y1,x1)
        for y in range(h):
            if A[y][0]==1:
                dfs(y,0)
            if A[y][w-1]==1:
                dfs(y,w-1)
        for x in range(w):
            if A[0][x]==1:
                dfs(0,x)
            if A[h-1][x]==1:
                dfs(h-1,x)
        return sum(map(sum,A))
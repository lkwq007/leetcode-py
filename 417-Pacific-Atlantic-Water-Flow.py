class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        ret=[]
        if len(matrix)<1 or len(matrix[0])<1:
            return ret
        # visited array
        h=len(matrix)
        w=len(matrix[0])
        template=[0]*w
        visited=[template[:] for _ in range(h)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(y0,x0,second=False):
            current=2 if second else 1
            if second and visited[y0][x0]==1:
                ret.append([y0,x0])
            visited[y0][x0]=current
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w and visited[y1][x1]!=current and matrix[y1][x1]>=matrix[y0][x0]:
                    dfs(y1,x1,second)
        # pacific
        for y in range(h):
            dfs(y,0)
        for x in range(w):
            dfs(0,x)
        # atlantic
        for y in range(h):
            dfs(y,w-1,True)
        for x in range(w):
            dfs(h-1,x,True)
        return ret
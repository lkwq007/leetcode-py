class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # BFS
        cur=grid[0][0]
        queue=[(0,0)]
        offset=[(0,1),(1,0),(-1,0),(0,-1)]
        visited={}
        visited[(0,0)]=1
        n=len(grid)
        boundary=set([])
        while queue:
            target=[]
            for y,x in queue:
                for yo,xo in offset:
                    yn=y+yo
                    xn=x+xo
                    if 0<=yn<n and 0<=xn<n:
                        if grid[yn][xn]<=cur and (yn,xn) not in visited:
                            if yn==n-1 and xn==n-1:
                                return cur
                            visited[(yn,xn)]=1
                            target.append((yn,xn))
                        elif grid[yn][xn]>cur:
                            boundary.add((y,x))
            # print(cur,queue,target,boundary)
            if len(target)==0:
                cur+=1
                queue=list(boundary)
                boundary=set([])
            else:
                queue=target

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # DFS
        cur=grid[0][0]
        n=len(grid)
        self.visited={}
        offset=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(y,x,t):
            if y==n-1 and x==n-1:
                return True
            self.visited[(y,x)]=1
            for yo,xo in offset:
                yn=y+yo
                xn=x+xo
                if 0<=yn<n and 0<=xn<n and grid[yn][xn]<=t and (yn,xn) not in self.visited:
                    if dfs(yn,xn,t):
                        return True
            return False
        for i in range(cur,n*n):
            self.visited={}
            if dfs(0,0,i):
                return i
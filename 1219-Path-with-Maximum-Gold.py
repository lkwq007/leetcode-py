class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ret=0
        # brute force
        h=len(grid)
        w=len(grid[0])
        # There are at most 25 cells containing gold.
        self.ret=0
        record={}
        offset=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(y,x):
            record[(y,x)]=1
            ret=grid[y][x]
            acc=0
            for yo,xo in offset:
                yn=y+yo
                xn=x+xo
                if 0<=yn<h and 0<=xn<w and grid[yn][xn]>0 and record.get((yn,xn),0)==0:
                    acc=max(acc,dfs(yn,xn))
            record[(y,x)]=0
            return ret+acc
        for y in range(h):
            for x in range(w):
                if grid[y][x]>0:
                    record.clear()
                    self.ret=max(self.ret,dfs(y,x))
        return self.ret




# class Solution:
#     def getMaximumGold(self, grid: List[List[int]]) -> int:
#         self.ret=0
#         # brute force
#         h=len(grid)
#         w=len(grid[0])
#         offset=[(1,0),(0,1),(-1,0),(0,-1)]
#         def adjacency(y0,x0):
#             cnt=0
#             lst=[]
#             for y1,x1 in offset:
#                 y=y0+y1
#                 x=x0+x1
#                 if 0<=y<h and 0<=x<w and grid[y][x]>0:
#                     cnt+=1
#                     lst.append((y,x))
#             return cnt,lst

#         for y in range(h):
#             for x in range(w):
#                 if grid[y][x]>0:
#                     cnt,lst=adjacency(y,x)
#                     if cnt==0:
#                         self.ret=max(grid[y][x],self.ret)
#                         grid[y][x]=0
#                     elif cnt==1:
#                         y0,x0=lst[0]
#                         if adjacency(y0,x0)
#                         grid[y0][x0]+=grid[y][x]
#                         grid[y][x]=0
                    
#         return self.ret
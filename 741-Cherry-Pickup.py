from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if len(grid)<1 or len(grid[0])<1:
            return 0
        h=len(grid)
        w=len(grid[0])
        for y in range(h):
            for x in range(w):
                top=-1 if y==0 else grid[y-1][x]
                left=-1 if x==0 else grid[y][x-1]
                if x==0 and y==0:
                    left=0
                if left==-1 and top==-1:
                    grid[y][x]=-1
        if grid[-1][-1]==-1:
            return 0
        template=[0]*(w+1)
        dp=[template[:] for _ in range(w+1)]
        dp_last=[template[:] for _ in range(w+1)]
        dp_last[0][0]=grid[0][0]
        for y in range(h):
            for i in range(0,w):
                for j in range(i,w):
                    if grid[y][i]==-1 or grid[y][j]==-1:
                        dp[i][j]=-1
                    left_i=-1 if i==0 else dp[i-1][j]
                    top_i=-1 if y==0 else dp_last[i][j] 
# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         if len(grid)<1 or len(grid[0])<1:
#             return 0
#         h=len(grid)
#         w=len(grid[0])
#         template=[0]*w
#         dp=[template[:] for _ in range(h)]
#         for y in range(0,h):
#             for x in range(0,w):
#                 top=-1 if y==0 else dp[y-1][x]
#                 left=-1 if x==0 else dp[y][x-1]
#                 if y==0 and x==0:
#                     top=0
#                 if (top==-1 and left==-1) or grid[y][x]==-1:
#                     grid[y][x]=-1
#                     dp[y][x]=-1
#                 else:
#                     dp[y][x]=max(top,left)+grid[y][x]
#         if dp[-1][-1]==-1:
#             return 0
#         ret=dp[-1][-1]
#         def dfs(y,x):
#             if y==0 and x==0:
#                 grid[y][x]=0
#                 return
#             if y==0:
#                 grid[y][x]=0
#                 dfs(y,x-1)
#             elif x==0:
#                 grid[y][x]=0
#                 dfs(y-1,x)
#             elif dp[y][x]>=0 and dp[y-1][x]+grid[y][x]==dp[y][x]:
#                 grid[y][x]=0
#                 dfs(y-1,x)
#             elif dp[y][x]>=0 and dp[y][x-1]+grid[y][x]==dp[y][x]:
#                 grid[y][x]=0
#                 dfs(y,x-1)
#         dfs(h-1,w-1)
#         dp=[0]*w
#         last=[-1]*w
#         last[-1]=0
#         for y in range(h-1,-1,-1):
#             for x in range(w-1,-1,-1):
#                 bottom=last[x]
#                 right=-1 if x+1>w-1 else dp[x+1]
#                 if (bottom==-1 and right==-1) or grid[y][x]==-1:
#                     grid[y][x]=-1
#                     dp[x]=-1
#                 else:
#                     dp[x]=max(bottom,right)+grid[y][x]
#             tmp=last
#             last=dp
#             dp=tmp
#         return ret+last[0]
grid=[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]

x=Solution()
print(x.cherryPickup(grid))
# from typing import List
# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         if len(grid)<1 or len(grid[0])<1:
#             return 0
#         h=len(grid)
#         w=len(grid[0])
#         dp=[0]*w
#         last=[-1]*w
#         last[0]=0
#         for y in range(0,h):
#             print(grid)
#             for x in range(0,w):
#                 top=last[x]
#                 left=-1 if x==0 else dp[x-1]
#                 if (top==-1 and left==-1) or grid[y][x]==-1:
#                     grid[y][x]=-1
#                     dp[x]=-1
#                 else:
#                     dp[x]=max(top,left)+grid[y][x]
#                     grid[y][x]=0
#             tmp=last
#             last=dp
#             dp=tmp
#         if last[-1]==-1:
#             return 0
#         ret=last[-1]
#         dp=[0]*w
#         last=[-1]*w
#         last[-1]=0
#         for y in range(h-1,-1,-1):
#             for w in range(w-1,-1,-1):
#                 bottom=last[x]
#                 right=-1 if x>=w-1 else dp[x+1]
#                 if (bottom==-1 and right==-1) or grid[y][x]==-1:
#                     grid[y][x]=-1
#                     dp[x]=-1
#                 else:
#                     dp[x]=max(bottom,right)+grid[y][x]
#                     grid[y][x]=0
#             tmp=last
#             last=dp
#             dp=tmp
#         print(grid,last)
        
#         return ret+last[0]
# grid=[[0, 1, -1],
#  [1, 0, -1],
#  [1, 1,  1]]

# x=Solution()
# print(x.cherryPickup(grid))
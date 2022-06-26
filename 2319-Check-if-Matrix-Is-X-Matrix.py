class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        record={}
        for i in range(n):
            record[(i,i)]=1
            record[(i,n-i-1)]=1
            if grid[i][i]==0 or grid[i][n-i-1]==0:
                return False
        for y in range(n):
            for x in range(n):
                if (y,x) not in record and grid[y][x]!=0:
                    return False
        return True
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        for y in range(n):
            for x in range(n):
                if ((x==y) or (x+y+1==n)):
                    if grid[y][x]==0:
                        return False
                else:
                    if grid[y][x]!=0:
                        return False
        return True
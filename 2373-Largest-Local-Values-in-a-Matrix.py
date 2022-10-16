class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def pool(y,x):
            acc=grid[y][x]
            for i in range(y-1,y+2):
                for j in range(x-1,x+2):
                    acc=max(grid[i][j],acc)
            return acc
        return [[pool(y,x) for x in range(1,len(grid)-1)] for y in range(1,len(grid)-1)]
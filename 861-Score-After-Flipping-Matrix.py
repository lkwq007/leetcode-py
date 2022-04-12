class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ret=len(grid)
        for i in range(1,len(grid[0])):
            ones=0
            for j in range(len(grid)):
                if grid[j][0]==0:
                    ones+=1-grid[j][i]
                else:
                    ones+=grid[j][i]
            ones=max(ones,len(grid)-ones)
            ret=ret*2+ones
        return ret
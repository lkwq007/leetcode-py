class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        grid=[sorted(item) for item in grid]
        ret=0
        for i in range(len(grid[0])):
            acc=grid[0][i]
            for j in range(len(grid)):
                acc=max(grid[j][i],acc)
            ret+=acc
        return ret
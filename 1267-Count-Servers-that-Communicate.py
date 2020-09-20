class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # three pass, O(1) space
        row=[sum(item) for item in grid]
        col=[sum(item) for item in zip(*grid)]
        total=sum(row)
        acc=0
        for i in range(len(row)):
            if row[i]==1:
                for j in range(len(col)):
                    if col[j]==1 and grid[i][j]==1:
                        acc+=1
        return total-acc

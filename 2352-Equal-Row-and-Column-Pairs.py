class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # brute force
        row={}
        for y in range(len(grid)):
            cur=tuple(grid[y])
            row[cur]=row.get(cur,0)+1
        ret=0
        for x in range(len(grid)):
            lst=tuple(grid[y][x] for y in range(len(grid)))
            ret+=row.get(lst,0)
        return ret
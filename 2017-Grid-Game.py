class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        lacc=0
        racc=0
        rtotal=sum(grid[1])
        ltotal=sum(grid[0])
        ret=rtotal

        for i in range(len(grid[0])):
            lacc+=grid[0][i]
            ltotal-=grid[0][i]
            tmp=lacc+rtotal
            rtotal-=grid[1][i]
            ret=min(max(ltotal,racc),ret)
            racc+=grid[1][i]
        return ret
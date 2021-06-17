class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        ret=1
        h=len(grid)
        w=len(grid[0])
        template=[0]*(w+1)
        row=[template[:] for _ in range(h+1)]
        col=[template[:] for _ in range(h+1)]
        diag=[template[:] for _ in range(h+1)]
        for y in range(h):
            acc=0
            for x in range(w):
                acc+=grid[y][x]
                row[y][x]=acc
        for x in range(w):
            acc=0
            for y in range(h):
                acc+=grid[y][x]
                col[y][x]=acc
        for y0 in range(h):
            for x0 in range(w):
                edge=2
                while y0+edge<=h and x0+edge<=w:
                    acc=0
                    racc=0
                    for i in range(edge):
                        acc+=grid[y0+i][x0+i]
                        racc+=grid[y0+i][x0+(edge-i-1)]
                    if acc!=racc:
                        edge+=1
                        continue
                    flag=False
                    for i in range(edge):
                        if acc!=(row[y0+i][x0+edge-1]-row[y0+i][x0-1]) or acc!=(col[y0+edge-1][x0+i]-col[y0-1][x0+i]):
                            flag=True
                            break
                    if not flag:
                        ret=max(edge,ret)
                    edge+=1
        return ret
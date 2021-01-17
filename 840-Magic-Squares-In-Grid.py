class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # brute force
        h=len(grid)
        w=len(grid[0])
        if h<3 or w<3:
            return 0
        ret=0
        def check(y0,x0):
            record={}
            acc=0
            for y in range(y0-1,y0+2):
                for x in range(x0-1,x0+2):
                    if grid[y][x] in record or not (1<=grid[y][x]<=9):
                        return 0
                    record[grid[y][x]]=1
            for y in range(y0-1,y0+2):
                acc+=grid[y][x0]
            for y in range(y0-1,y0+2):
                tmp=0
                for x in range(x0-1,x0+2):
                    tmp+=grid[y][x]
                if tmp!=acc:
                    return 0
            for x in range(x0-1,x0+2):
                tmp=0
                for y in range(y0-1,y0+2):
                    tmp+=grid[y][x]
                if tmp!=acc:
                    return 0
            lst=[-1,0,1]
            for offset in (lst,lst[::-1]):
                tmp=0
                for i in offset:
                    tmp+=grid[y0+i][x0+i]
                if tmp!=acc:
                    return 0
            return 1
        for y in range(1,h-1):
            for x in range(1,w-1):
                ret+=check(y,x)
        return ret
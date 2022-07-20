class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        h=len(grid)
        w=len(grid[0])
        layers=min(h,w)//2
        def next(y,x,l,step=1):
            if y==l:
                d=0 if x>l else 1
            elif x==l:
                d=1 if y<h-l-1 else 2
            elif y==h-l-1:
                d=2 if x<w-l-1 else 3
            else:
                d=3 if y>l else 0
            match d:
                case 0:
                    if x-step>=l:
                        return y,x-step
                    return next(y,l,l,step-(x-l))
                case 1:
                    if y+step<=h-l-1:
                        return y+step,x
                    return next(h-l-1,x,l,step-(h-l-1-y))
                case 2:
                    if x+step<=w-l-1:
                        return y,x+step
                    return next(y,w-l-1,l,step-(w-l-1-x))
                case 3:
                    if y-step>=l:
                        return y-step,x
                    return next(l,x,l,step-(y-l))
        for l in range(layers):
            m=h-l*2
            n=w-l*2
            total=2*m+2*n-4
            move=((k%total))%total
            # inplace?
            y0,x0=l,l
            for i in range(total):
                y,x=y0,x0
                last=grid[y][x]
                if last>0:
                    y,x=next(y,x,l,move)
                    while grid[y][x]>0:
                        tmp=grid[y][x]
                        grid[y][x]=-last
                        last=tmp
                        y,x=next(y,x,l,move)
                y0,x0=next(y0,x0,l)
        for y in range(h):
            for x in range(w):
                grid[y][x]=-grid[y][x]
        return grid


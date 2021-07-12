class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue=[entrance]
        step=0
        offset=[(0,1),(1,0),(-1,0),(0,-1)]
        h=len(maze)
        w=len(maze[0])
        y0,x0=entrance
        maze[y0][x0]="+"
        while queue:
            step+=1
            target=[]
            for y,x in queue:
                for yo,xo in offset:
                    yn=y+yo
                    xn=x+xo
                    if 0<=yn<h and 0<=xn<w and maze[yn][xn]==".":
                        maze[yn][xn]="+"
                        if yn==0 or yn==h-1 or xn==0 or xn==w-1:
                            return step
                        target.append((yn,xn))
            queue=target
        return -1
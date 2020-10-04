class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        h=len(mat)
        w=len(mat[0])
        step=0
        masks=[]
        full=(1<<(h*w))-1
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        inital=0
        for y0 in range(h):
            for x0 in range(w):
                if mat[y0][x0]==1:
                    inital|=(1<<(y0*w+x0))
                mask=0
                mask=mask|(1<<(y0*w+x0))
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    if 0<=y1<h and 0<=x1<w:
                        mask=mask|(1<<(y1*w+x1))
                masks.append(mask)
        queue=[inital]
        visited={}
        visited[inital]=0
        if inital==0:
            return 0
        while queue:
            step+=1
            target=[]
            for state in queue:
                for mask in masks:
                    next=(state^mask)
                    if next==0:
                        return step
                    if next not in visited:
                        visited[next]=step
                        target.append(next)
            queue=target
        return -1

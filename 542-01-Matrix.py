class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        h=len(matrix)
        w=len(matrix[0])
        queue=[]
        for y in range(h):
            for x in range(w):
                if matrix[y][x]==0:
                    queue.append((y,x))
                else:
                    matrix[y][x]=-1
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            target=[]
            record={}
            for y0,x0 in queue:
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    cur=matrix[y0][x0]
                    if 0<=y1<h and 0<=x1<w and matrix[y1][x1]!=0:
                        if matrix[y1][x1]==-1 or matrix[y1][x1]>cur+1:
                            matrix[y1][x1]=cur+1
                            if (y1,x1) not in record:
                                record[(y1,x1)]=1
                                target.append((y1,x1))
            queue=target
        return matrix

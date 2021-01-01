class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # brute force
        h=len(mat)
        w=len(mat[0])
        def fill(y0,x0):
            y,x=y0,x0
            lst=[]
            while x<w and y<h:
                lst.append(mat[y][x])
                y+=1
                x+=1
            lst.sort()
            y,x=y0,x0
            for item in lst:
                mat[y][x]=item
                y+=1
                x+=1
        for i in range(w):
            fill(0,w-i-1)
        for i in range(1,h):
            fill(i,0)
        return mat
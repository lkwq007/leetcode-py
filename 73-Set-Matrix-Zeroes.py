class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)<1 or len(matrix[0])<1:
            return
        h=len(matrix)
        w=len(matrix[0])
        zero_row=-1
        zero_col=-1
        for y in range(h):
            for x in range(w):
                if matrix[y][x]==0 and zero_row<0:
                    zero_row=y
                    zero_col=x
                elif matrix[y][x]==0:
                    matrix[zero_row][x]=0
                    matrix[y][zero_col]=0
        if zero_row<0:
            return
        for x in range(w):
            if x!=zero_col and matrix[zero_row][x]==0:
                for y in range(h):
                    matrix[y][x]=0
        for y in range(h):
            if y!=zero_row and matrix[y][zero_col]==0:
                for x in range(w):
                    matrix[y][x]=0
        for x in range(w):
            matrix[zero_row][x]=0
        for y in range(h):
            matrix[y][zero_col]=0
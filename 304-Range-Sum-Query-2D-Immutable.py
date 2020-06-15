class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix)<1 or len(matrix[0])<1:
            self.matrix=[[0]]
            return
        h=len(matrix)
        w=len(matrix[0])
        for y in range(0,h):
            acc=0
            for x in range(0,w):
                acc+=matrix[y][x]
                top=0 if y==0 else matrix[y-1][x]
                matrix[y][x]=acc+top
        self.matrix=matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total=self.matrix[row2][col2]
        left=0 if col1==0 else self.matrix[row2][col1-1]
        right=0 if row1==0 else self.matrix[row1-1][col2]
        extra=0 if col1==0 or row1==0 else self.matrix[row1-1][col1-1]
        return total-left-right+extra

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
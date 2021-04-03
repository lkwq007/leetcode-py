# atmost 500 ops -> lazy query
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect=rectangle
        self.log=[]

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.log.append((row1,col1,row2,col2,newValue))

    def getValue(self, row: int, col: int) -> int:
        total=len(self.log)
        for i in range(total-1,-1,-1):
            item=self.log[i]
            if item[0]<=row<=item[2] and item[1]<=col<=item[3]:
                return item[-1]
        return self.rect[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
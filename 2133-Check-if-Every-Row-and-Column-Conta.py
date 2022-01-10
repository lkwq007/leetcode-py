class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        total=len(matrix)
        lst=[0]*(total+1)
        row=lst[:]
        col=lst[:]
        for y in range(total):
            for x in range(total):
                if 1<=matrix[y][x]<=total and row[matrix[y][x]]==0:
                    row[matrix[y][x]]=1
                else:
                    return False
                if 1<=matrix[x][y]<=total and col[matrix[x][y]]==0:
                    col[matrix[x][y]]=1
                else:
                    return False
            row=lst[:]
            col=lst[:]
        return True
                
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)<1 or len(matrix[0])<1:
            return False
        h=len(matrix)
        w=len(matrix[0])
        left=0
        right=h-1
        while left<right:
            middle=left+(right-left)//2
            if matrix[middle][0]<target:
                left=middle+1
            elif matrix[middle][0]>target:
                right=middle-1
            else:
                return True
        row=left
        left=0
        right=w-1
        while left<right:
            middle=left+(right-left)//2
            if matrix[row][middle]<target:
                left=middle+1
            elif matrix[row][middle]>target:
                right=middle-1
            else:
                return True
        return matrix[row][left]==target
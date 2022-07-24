class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        h=len(matrix)
        w=len(matrix[0])
        for y in range(h):
            for x in range(w):
                if matrix[y][x]==target:
                    return True
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h=len(matrix)
        w=len(matrix[0])
        y=0
        x=w-1
        while y<h and x>=0:
            if matrix[y][x]==target:
                return True
            if matrix[y][x]>target:
                x-=1
            else:
                y+=1
        return False
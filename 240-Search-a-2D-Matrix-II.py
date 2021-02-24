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
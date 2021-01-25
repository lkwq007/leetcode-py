class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # dp
        h=len(matrix)
        w=len(matrix[0])
        lst=[matrix[0][0]]
        for x in range(1,w):
            matrix[0][x]^=matrix[0][x-1]
            lst.append(matrix[0][x])
        for y in range(1,h):
            matrix[y][0]^=matrix[y-1][0]
            lst.append(matrix[y][0])
        for y in range(1,h):
            for x in range(1,w):
                matrix[y][x]=matrix[y][x]^matrix[y][x-1]^matrix[y-1][x]^matrix[y-1][x-1]
                lst.append(matrix[y][x])
        lst.sort(key=lambda x:-x)
        return lst[k-1]
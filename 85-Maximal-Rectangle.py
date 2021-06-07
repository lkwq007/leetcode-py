class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        h=len(matrix)
        w=len(matrix[0])
        template=[0]*w
        dp_y=[template[:] for _ in range(h)]
        dp_x=[template[:] for _ in range(h)]
        dp_y[0][0]=1 if matrix[0][0]=="1" else 0
        dp_x[0][0]=dp_x[0][0]
        for y in range(h):
            for x in range(w):
                if matrix[y][x]=="1":
                    
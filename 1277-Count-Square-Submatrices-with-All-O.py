from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix)<1 or len(matrix[0])<1:
            return 0
        cnt=0
        h=len(matrix)
        w=len(matrix[0])
        for i in range(0,w):
            cnt+=matrix[0][i]
        for i in range(1,h):
            cnt+=matrix[i][0]
        for y in range(1,h):
            for x in range(1,w):
                if matrix[y][x]:
                    matrix[y][x]=min(matrix[y-1][x],matrix[y][x-1],matrix[y-1][x-1])+1
                cnt+=matrix[y][x]
        return cnt

mat=[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
x=Solution()
x.countSquares(mat)
print(mat)
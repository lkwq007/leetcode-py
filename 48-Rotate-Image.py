from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        middle=(n//2)
        for layer in range(0,middle):
            size=n-2*layer
            for idx in range(0,size-1):
                tmp=matrix[layer][layer+idx]
                matrix[layer][layer+idx]=matrix[layer+size-idx-1][layer]
                matrix[layer+size-idx-1][layer]=matrix[n-layer-1][layer+size-idx-1]
                matrix[n-layer-1][layer+size-idx-1]=matrix[layer+idx][n-layer-1]
                matrix[layer+idx][n-layer-1]=tmp
        return
x=Solution()
tmp=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
x.rotate(tmp)
print(tmp)
print(list(zip(*tmp)))

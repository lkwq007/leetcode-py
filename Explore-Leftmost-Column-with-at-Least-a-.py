# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
   def get(self, x: int, y: int) -> int:
       return 9
   def dimensions(self) -> []:
       return []
    
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        lst=binaryMatrix.dimensions()
        n=lst[0]
        m=lst[1]
        right=m-1
        exist=False
        for y in range(0,n):
            left=0
            flag=binaryMatrix.get(y,right)
            if flag==0:
                continue
            exist=True
            while left<right:
                middle=(left+right)//2
                flag=binaryMatrix.get(y,middle)
                if flag==1:
                    right=middle
                else:
                    if left==middle:
                        break
                    left=middle
        if exist:
            return right
        return -1

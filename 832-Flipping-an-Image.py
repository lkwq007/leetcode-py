from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if len(A)<1 or len(A[0])<1:
            return A
        h=len(A)
        w=len(A[0])
        template=[0]*w
        ret=[template[:] for _ in range(h)]
        for y in range(0,h):
            for x in range(0,w):
                ret[y][w-x-1]=1-A[y][x]
                ret[y][x]=1-A[y][w-x-1]
        return ret
x=Solution()
print(x.flipAndInvertImage([[1,1,0]]))
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        h=len(mat)
        w=len(mat[0])
        def peak(y):
            left=0
            right=w-1
            while left<right:
                middle=left+(right-left)//2
                if mat[y][middle]>mat[y][middle+1]:
                    right=left
                else:
                    left=middle+1
            return left
        for y in range(h):
            x=peak(y)
            print(x)
            top=-1 if y==0 else mat[y-1][x]
            bottom=-1 if y==h-1 else mat[y+1][x]
            if mat[y][x]>top and mat[y][x]>bottom:
                return [y,x]
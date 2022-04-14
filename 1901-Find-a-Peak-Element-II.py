class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        h=len(mat)
        w=len(mat[0])
        def search(left,right):
            middle=left+(right-left)//2
            y,x=0,middle
            for i in range(h):
                l=max(0,middle-1)
                r=min(w,middle+2)
                for j in range(l,r):
                    if mat[y][x]<mat[i][j]:
                        y,x=i,j
                    if mat[y][x]==mat[i][j] and j==middle:
                        y,x=i,j
            if x==middle:
                return [y,x]
            elif x<middle:
                return search(left,middle-1)
            return search(middle+1,right)
        return search(0,w-1)
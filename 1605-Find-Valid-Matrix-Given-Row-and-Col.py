class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        h=len(rowSum)
        w=len(colSum)
        mat=[[0]*w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                tmp=min(rowSum[y],colSum[x])
                rowSum[y]-=tmp
                colSum[x]-=tmp
                mat[y][x]=tmp
        return mat
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=len(mat)
        ret=0
        for i in range(total):
            ret+=mat[i][i]+mat[i][total-i-1]
        if total%2==1:
            ret-=mat[total//2][total//2]
        return ret
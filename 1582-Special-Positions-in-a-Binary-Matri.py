class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row=[sum(x) for x in mat]
        col=[sum(x) for x in zip(*mat)]
        ret=0
        for i in range(len(mat)):
            if row[i]==1:
                for j in range(len(mat[0])):
                    if col[j]==1 and mat[i][j]==1:
                        ret+=1
        return ret
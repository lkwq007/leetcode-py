class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows=[0]*len(mat)
        cols=[0]*len(mat[0])
        record={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                record[mat[i][j]]=(i,j)
        for idx,item in enumerate(arr):
            i,j=record[item]
            rows[i]+=1
            cols[j]+=1
            if rows[i]==len(mat[0]) or cols[j]==len(mat):
                return idx
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        N=len(mat)
        def check(loc):
            for i in range(N):
                for j in range(N):
                    if loc(mat,i,j)!=target[i][j]:
                        return False
            return True
        def rot0(mat,i,j):
            return mat[i][j]
        def rot1(mat,i,j):
            return mat[N-i-1][N-j-1]
        def rot2(mat,i,j):
            return mat[j][N-i-1]
        def rot3(mat,i,j):
            return mat[N-j-1][i]
        for func in [rot0,rot1,rot2,rot3]:
            if check(func):
                return True
        return False
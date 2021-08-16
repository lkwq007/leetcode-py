class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ret=0
        h=len(mat)
        w=len(mat[0])
        template=[0]*(w+1)
        left=[template[:] for y in range(h+1)]
        top=[template[:] for y in range(h+1)]
        for y in range(h):
            for x in range(w):
                if mat[y][x]==1:
                    top[y][x]=top[y-1][x]+1
                    left[y][x]=left[y][x-1]+1
                    acc=left[y][x]
                    for i in range(top[y][x]):
                        acc=min(acc,left[y-i][x])
                        ret+=acc
        return ret
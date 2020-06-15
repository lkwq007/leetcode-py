from typing import List
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if len(mat)<1 or len(mat[0])<1:
            return mat
        h=len(mat)
        w=len(mat[0])
        template=[0]*w
        acc_sum=[template[:] for i in range(0,h)]
        ret=[template[:] for i in range(0,h)]
        for y in range(0,h):
            acc=0
            for x in range(0,w):
                acc+=mat[y][x]
                tmp=acc_sum[y-1][x] if y>0 else 0
                acc_sum[y][x]=acc+tmp
        for y in range(0,h):
            for x in range(0,w):
                total=acc_sum[min(y+K,h-1)][min(x+K,w-1)]
                top=0 if y<=K else acc_sum[y-K-1][min(x+K,w-1)]
                left=0 if x<=K else acc_sum[min(y+K,h-1)][x-K-1]
                overlap= 0 if x<=K or y<=K else acc_sum[y-K-1][x-K-1]
                ret[y][x]=total+overlap-top-left
        return ret
x=Solution()
print(x.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],1))

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if len(mat)<1 or len(mat[0])<1:
            return mat
        h=len(mat)
        w=len(mat[0])
        dp=[0]*w
        dp_next=dp[:]
        ret=[dp[:] for i in range(0,h)]
        for x in range(0,w):
            for y in range(0,K+1):
                dp[x]+=mat[y][x]
        for y in range(0,h):
            for x in range(0,w):
                if x==0:
                    for idx in range(0,min(K+1,w)):
                        ret[y][x]+=dp[idx]
                else:
                    left=dp[x-1-K] if x-1>=K else 0
                    right=dp[x+K] if x+K<w else 0
                    ret[y][x]=ret[y][x-1]-left+right
                top=mat[y-K][x] if y>=K else 0
                bottom=mat[y+1+K][x] if y+1+K<h else 0
                dp_next[x]=dp[x]-top+bottom
            tmp=dp
            dp=dp_next
            dp_next=tmp
        return ret
                
x=Solution()
print(x.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],1))
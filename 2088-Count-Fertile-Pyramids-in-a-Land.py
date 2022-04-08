class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def calc(arr):
            ret=0
            h=len(arr)
            w=len(arr[0])
            dp=[[0]*w for _ in range(h)]
            for i in range(1,w-1):
                if arr[0][i]==1:
                    dp[0][i]=1
            for i in range(1,h):
                acc=0
                for j in range(w):
                    if arr[i][j]==0:
                        acc=0
                    else:
                        acc+=1
                        if j>0:
                            dp[i][j]=1
                        if j>0 and dp[i-1][j-1]>0:
                            last=dp[i-1][j-1]
                            cur=(acc-1)//2
                            if cur>=last:
                                dp[i][j]=last+1
                            else:
                                dp[i][j]=cur+1
                            ret+=dp[i][j]-1
            # print(dp)
            # print(ret)
            return ret
        return calc(grid)+calc(list(reversed(grid)))
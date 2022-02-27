class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        template=[f for f,t in tires]
        dp=[template[:] for _ in range(numLaps)]
        # 2 <= ri <= 105
        # using one tire
        for i in range(len(tires)):
            f,r=tires[i]
            acc=f
            for j in range(1,numLaps):
                acc*=r
                dp[j][i]=dp[j-1][i]+acc
                acc=min(acc,10**15)
        for i in range(1,numLaps):
            minval=min(dp[i-1])
            for j in range(len(tires)):
                f,r=tires[j]
                dp[i][j]=min(dp[i][j],minval+changeTime+f)
                last=0
                acc=f
                for k in range(i,numLaps):
                    dp[k][j]=min(dp[k][j],minval+changeTime+acc+last)
                    last=acc+last
                    acc=acc*r
                    if acc>2*changeTime:
                        break
        return min(dp[-1])
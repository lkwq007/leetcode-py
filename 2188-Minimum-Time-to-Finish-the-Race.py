class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        record={}
        for f,r in tires:
            if f not in record:
                record[f]=r
            record[f]=min(r,record[f])
        tires=[(k,v) for k,v in record.items()]
        record={}
        for f,r in tires:
            if r not in record:
                record[r]=f
            record[r]=min(f,record[r])
        tires=[(v,k) for k,v in record.items()]
        cost=[10**9]*numLaps
        for i in range(len(tires)):
            f,r=tires[i]
            acc=f
            last=f
            cost[0]=min(f,cost[0])
            for j in range(1,numLaps):
                acc*=r
                cur=last+acc
                cost[j]=min(cur,cost[j])
                last=cur
                if cur>=(j+1)*(f+changeTime):
                    break
        dp=cost[:]
        for i in range(1,numLaps):
            acc=0
            base=changeTime+dp[0]
            for j in range(i-1,-1,-1):
                acc+=base
                if cost[i-j-1]>=acc:
                    break
                dp[i]=min(dp[i],dp[j]+cost[i-j-1]+changeTime)
        return dp[-1]

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        record={}
        for f,r in tires:
            if f not in record:
                record[f]=r
            record[f]=min(r,record[f])
        tires=[(k,v) for k,v in record.items()]
        record={}
        for f,r in tires:
            if r not in record:
                record[r]=f
            record[r]=min(f,record[r])
        tires=[(v,k) for k,v in record.items()]
        template=[10**9 for f,t in tires]
        tbl=[template[:] for _ in range(numLaps)]
        cost=[0]*numLaps
        # 2 <= ri <= 105
        # using one tire
        for i in range(len(tires)):
            tbl[0][i]=tires[i][0]
        for i in range(len(tires)):
            f,r=tires[i]
            acc=f
            for j in range(1,numLaps):
                acc*=r
                tbl[j][i]=tbl[j-1][i]+acc
                if tbl[j][i]>10**9:
                    # tbl[j][i]=10**15
                    acc=0
                    break
        for i in range(numLaps):
            cost[i]=min(tbl[i])
        dp=cost[:]
        for i in range(1,numLaps):
            acc=0
            base=changeTime+dp[0]
            for j in range(i-1,-1,-1):
                acc+=base
                if cost[i-j-1]>=acc:
                    break
                dp[i]=min(dp[i],dp[j]+cost[i-j-1]+changeTime)
        return dp[-1]
# class Solution:
#     def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
#         # TLE
#         template=[f for f,t in tires]
#         dp=[template[:] for _ in range(numLaps)]
#         # 2 <= ri <= 105
#         # using one tire
#         for i in range(len(tires)):
#             f,r=tires[i]
#             acc=f
#             for j in range(1,numLaps):
#                 acc*=r
#                 dp[j][i]=dp[j-1][i]+acc
#                 acc=min(acc,10**15)
#         for i in range(1,numLaps):
#             minval=min(dp[i-1])
#             for j in range(len(tires)):
#                 f,r=tires[j]
#                 dp[i][j]=min(dp[i][j],minval+changeTime+f)
#                 last=0
#                 acc=f
#                 for k in range(i,numLaps):
#                     dp[k][j]=min(dp[k][j],minval+changeTime+acc+last)
#                     last=acc+last
#                     acc=acc*r
#                     if acc>2*changeTime:
#                         break
#         return min(dp[-1])
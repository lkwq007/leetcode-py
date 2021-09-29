class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # rides.sort(key=lambda x:(x[1],x[0]))
        dp=[0]*(n+1)
        record={}
        for start,end,tip in rides:
            if end not in record:
                record[end]=[]
            record[end].append((start,tip))
        ret=0
        for i in range(1,n+1):
            dp[i]=max(dp[i],dp[i-1])
            if i in record:
                for start,tip in record[i]:
                    dp[i]=max(dp[i],dp[start]+tip+i-start)
        # print(dp)
        return dp[-1]
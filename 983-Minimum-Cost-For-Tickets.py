class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0]*366
        idx=1
        for day in days:
            while idx<day:
                dp[idx]=dp[idx-1]
                idx+=1
            dp[day]=min(dp[day-1]+costs[0],dp[max(day-7,0)]+costs[1],dp[max(day-30,0)]+costs[2])
            idx=day+1
        return dp[days[-1]]
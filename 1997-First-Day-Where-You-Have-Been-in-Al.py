class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        if len(nextVisit)<2:
            return 0
        term=10**9+7
        # nextVisit[i] where 0 <= nextVisit[i] <= i
        total=0
        n=len(nextVisit)
        dp=[1]*(n+1)
        first=[0]*(n+1)
        prefix=[0]*(n+1)
        # from nextVisit[i] to i
        # first i, first i-1 + dp []
        for i in range(n-1):
            next=nextVisit[i]
            if next==i:
                dp[i]=1
            else:
                dp[i]=i-next+1+prefix[i-1]-prefix[next-1]
            dp[i]%=term
            prefix[i]=prefix[i-1]+dp[i]
            prefix[i]%=term
            first[i+1]=first[i]+dp[i]+1
            first[i+1]%=term
        return first[-2]
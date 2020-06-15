class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)<1 or len(triangle[0])<1:
            return 0
        row=len(triangle)
        dp=[0]*row
        last=[0]*row
        last[0]=triangle[0][0]
        for y in range(1,row):
            total=len(triangle[y])
            dp[0]=last[0]+triangle[y][0]
            if total-1!=0:
                dp[total-1]=last[total-2]+triangle[y][total-1]
            for x in range(1,total-1):
                cur=triangle[y][x]
                top=min(last[x-1],last[x])
                dp[x]=cur+top
            tmp=last
            last=dp
            dp=tmp
        return min(last)
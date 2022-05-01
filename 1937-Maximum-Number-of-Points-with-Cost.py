class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp=points[0][:]
        ret=max(dp)
        h=len(points)
        w=len(points[0])
        for y in range(1,h):
            target=[0]*w
            lst=[0]*(w+1)
            for x in range(w-1,-1,-1):
                lst[x]=max(dp[x],lst[x+1]-1)
            lacc=0
            for x in range(w):
                target[x]=points[y][x]+max(lacc,lst[x])
                lacc=max(lacc-1,dp[x]-1)
            dp=target
        return max(dp)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # brute force, TLE
        dp=points[0][:]
        ret=max(dp)
        h=len(points)
        w=len(points[0])
        target=[0]*w
        for y in range(1,h):
            for x in range(w):
                target[x]=-w
                for i in range(w):
                    target[x]=max(target[x],points[y][x]+dp[i]-abs(i-x))
                ret=max(target[x],ret)
            dp,target=target,dp
        return ret
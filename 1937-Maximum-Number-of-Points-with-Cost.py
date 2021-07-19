class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # brute force
        dp=points[0][:]
        ret=max(dp)
        h=len(points)
        w=len(points[0])
        target=[0]*w
        for y in range(1,h):
            max_idx=-1
            for x in range(w):
                target[x]=-w
                if max_idx>=x:
                    pass
                else:
                    max_idx=0
                    for i in range(w):
                        if dp[i]-abs(i-x)>=dp[max_idx]-abs(max_idx-x):
                            max_idx=i
                target[x]=points[y][x]+dp[max_idx]-abs(max_idx-x)
                ret=max(ret,target[x])
            dp,target=target,dp
        return ret
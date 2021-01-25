class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ret=0
        for i in range(1,len(points)):
            y=abs(points[i][1]-points[i-1][1])
            x=abs(points[i][0]-points[i-1][0])
            ret+=max(y,x)
        return ret
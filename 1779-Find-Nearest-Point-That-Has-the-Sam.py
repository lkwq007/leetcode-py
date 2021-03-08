class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ret=-1
        diff=-1
        for i in range(len(points)):
            x0,y0=points[i]
            if x0==x and (diff==-1 or abs(y0-y)<diff):
                diff=abs(y0-y)
                ret=i
            if y0==y and (diff==-1 or abs(x0-x)<diff):
                diff=abs(x0-x)
                ret=i
        return ret
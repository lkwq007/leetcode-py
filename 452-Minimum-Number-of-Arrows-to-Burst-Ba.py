class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)<2:
            return len(points)
        points.sort()
        end=points[0][0]-1
        ret=0
        for a,b in points:
            if a<=end:
                end=min(end,b)
            else:
                end=b
                ret+=1
        return ret
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        record={}
        for x,y in points:
            record[x]=1
        keys=list(sorted(record.keys()))
        ret=0
        for i in range(len(keys)-1):
            ret=max(ret,keys[i+1]-keys[i])
        return ret

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ret=0
        for i in range(len(points)-1):
            ret=max(ret,points[i+1][0]-points[i][0])
        return ret
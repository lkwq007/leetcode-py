class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        record={}
        for y,x in points:
            if (y,x) in record:
                return False
            record[(y,x)]=1
        # a line
        p1=points[0]
        p2=points[1]
        p3=points[2]
        return (p3[1]-p1[1])*(p2[0]-p1[0])!=(p2[1]-p1[1])*(p3[0]-p1[0])
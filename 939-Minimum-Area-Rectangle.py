class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        record={}
        record_x={}
        record_y={}
        ret=0
        for y,x in points:
            record[(y,x)]=1
        for i in range(len(points)):
            for j in range(i):
                y1,x1=points[i]
                y2,x2=points[j]
                if y1==y2 or x1==x2:
                    continue
                if (y1,x2) in record and (y2,x1) in record:
                    area=abs((y1-y2)*(x1-x2))
                    if ret==0 or ret>area:
                        ret=area
        return ret
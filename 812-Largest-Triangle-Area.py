from math import sqrt
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ret=0
        def sqr(x):
            return x*x
        def calc(a,b,c):
            xa,ya=points[a]
            xb,yb=points[b]
            xc,yc=points[c]
            bottom=sqrt(sqr(xa-xb)+sqr(ya-yb))
            if xa==xb:
                height=abs(xc-xa)
            elif ya==yb:
                height=abs(yc-ya)
            else:
                # (x-xa)/(xb-xa)*(yb-ya)-y+ya=0
                A=1.0/(xb-xa)*(yb-ya)
                B=-1
                C=-xa/(xb-xa)*(yb-ya)+ya
                height=abs(xc/(xb-xa)*(yb-ya)-yc+C)/sqrt(sqr(A)+sqr(B))
            return height*bottom/2
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    ret=max(ret,calc(i,j,k))
        return ret
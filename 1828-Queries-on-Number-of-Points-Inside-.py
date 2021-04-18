class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ret=[]
        for x,y,r in queries:
            rs=r*r
            acc=0
            for xp,yp in points:
                if (xp-x)*(xp-x)+(yp-y)*(yp-y)<=rs:
                    acc+=1
            ret.append(acc)
        return ret
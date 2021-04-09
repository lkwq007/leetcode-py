from math import sqrt
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W=int(sqrt(area))
        while area%W!=0:
            W-=1
        return [area//W,W]
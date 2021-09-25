# brute force, nearly TLE
class DetectSquares:

    def __init__(self):
        self.record={}
        self.maxy=0
        self.maxx=0
        self.miny=1000
        self.minx=1000
    def add(self, point: List[int]) -> None:
        y,x=point
        self.record[(y,x)]=self.record.get((y,x),0)+1
        self.maxy=max(self.maxy,y)
        self.maxx=max(self.maxx,x)
        self.miny=min(self.miny,y)
        self.minx=min(self.minx,x)



    def count(self, point: List[int]) -> int:
        y0,x0=point
        ret=0
        for ys,xs in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for offset in range(1,1001):
                y1=y0+ys*offset
                x1=x0+xs*offset
                if not (self.miny<=y1<=self.maxy and self.minx<=x1<=self.maxx):
                    break
                acc=1
                for y,x in [(y1,x1),(y0,x1),(y1,x0)]:
                    acc*=self.record.get((y,x),0)
                ret+=acc
        return ret


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
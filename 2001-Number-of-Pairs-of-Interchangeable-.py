class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # order of width and height is fixed
        # 1 <= widthi, heighti <= 10^5
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        record={}
        ret=0
        for w,h in rectangles:
            f=gcd(w,h)
            tup=(w//f,h//f)
            ret+=record.get(tup,0)
            record[tup]=record.get(tup,0)+1
        return ret
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # line is not a rect
        def area(a):
            ax0,ay0,ax1,ay1=a
            return (ay1-ay0)*(ax1-ax0)
        if area(rec1)==0 or area(rec2)==0:
            return False
        def swap(a):
            return [a[1],a[0],a[3],a[2]]
        def check(a,b):
            ax0,ay0,ax1,ay1=a
            bx0,by0,bx1,by1=b
            return ((bx0<ax0<bx1) or (bx0<ax1<bx1)) and \
                (by0<ay0<by1 or by0<ay1<by1 or ay0<by0<ay1 or ay0<by1<ay1)
        a,b=rec1,rec2
        return check(a,b) or check(b,a) or check(swap(a),swap(b)) or check(swap(b),swap(a))

# class Solution:
#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
#         def check(a,b):
#             return a[0]<b[0]<a[2] and a[1]<b[1]<a[3] or \
#                 (a[0]<b[2]<a[2] and a[1]<b[3]<a[3])
#         def check2(a,b):
#             return (a[0]<b[0]<a[2] or a[0]<b[2]<a[2]) and \
#                 (a[1]<b[1]<a[3] or a[1]<b[3]<a[3])
#         return check(rec1,rec2) or check(rec2,rec1) or check2(rec1,rec2) or check2(rec2,rec1)

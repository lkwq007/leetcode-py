"""
# Definition for a QuadTree node.

"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid)
        # this is kind of slow, we can also scan each grid first
        def build(y0,x0,n):
            if n==1:
                val=grid[y0][x0]==1
                return Node(val,True,None,None,None,None)
            offset=n//2
            tl=build(y0,x0,offset)
            tr=build(y0,x0+offset,offset)
            bl=build(y0+offset,x0,offset)
            br=build(y0+offset,x0+offset,offset)
            flag=tl.isLeaf
            val=tl.val
            for item in (tl,tr,bl,br):
                if not item.isLeaf or val!=item.val:
                    flag=False
            if flag:
                return Node(val,True,None,None,None,None)
            else:
                return Node(False,False,tl,tr,bl,br)
        return build(0,0,n)
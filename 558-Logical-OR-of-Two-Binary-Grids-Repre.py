# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1 is None:
            return quadTree2
        if quadTree2 is None:
            return quadTree1
        if quadTree1.isLeaf and quadTree1.val or quadTree2.isLeaf and quadTree2.val:
            return Node(True,True,None,None,None,None)
        if quadTree1.isLeaf and not quadTree1.val:
            return quadTree2
        if quadTree2.isLeaf and not quadTree2.val:
            return quadTree1
        quadTree1.topLeft=self.intersect(quadTree1.topLeft,quadTree2.topLeft)
        quadTree1.topRight=self.intersect(quadTree1.topRight,quadTree2.topRight)
        quadTree1.bottomLeft=self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
        quadTree1.bottomRight=self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
        cnt=0
        node_cnt=0
        for item in [quadTree1.topLeft,quadTree1.topRight,quadTree1.bottomLeft,quadTree1.bottomRight]:
            if item and item.isLeaf:
                if item.val:
                    cnt-=1
                else:
                    cnt+=1
            if item:
                node_cnt+=1
        if cnt==4:
            return Node(False,True,None,None,None,None)
        elif cnt==-4:
            return Node(True,True,None,None,None,None)
        return quadTree1
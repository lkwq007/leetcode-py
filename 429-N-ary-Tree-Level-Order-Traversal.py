"""
# Definition for a Node.

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue=[(root,0)]
        idx=0
        ret=[]
        acc=[]
        cur=-1
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if cur!=depth:
                cur=depth
                if acc:
                    ret.append(acc)
                acc=[]
            acc.append(node.val)
            if node.children:
                for item in node.children:
                    if item:
                        queue.append((item,depth+1))
        if acc:
            ret.append(acc)
        return ret
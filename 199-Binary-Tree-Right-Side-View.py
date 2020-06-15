# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        queue=[(root,0)]
        idx=0
        cur=-1
        last=None
        ret=[]
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if cur!=depth:
                cur=depth
                if last:
                    ret.append(last.val)
            last=node
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        if last:
            ret.append(last.val)
        return ret
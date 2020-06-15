# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        if acc:
            ret.append(acc)
        return ret
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ret=[]
        queue=[(root,0)]
        cur=-1
        idx=0
        acc=[]
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if cur!=depth:
                if acc:
                    ret.append(acc)
                acc=[]
                cur=depth
            acc.append(node.val)
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        ret.append(acc)
        return ret[::-1]
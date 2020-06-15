# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue=[(root,0)]
        idx=0
        cur_depth=0
        acc=0
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if cur_depth!=depth:
                cur_depth=depth
                acc=0
            acc+=node.val
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        return acc
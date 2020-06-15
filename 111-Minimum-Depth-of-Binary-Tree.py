# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.min=None
        def depth(node,acc):
            if node.left is None and node.right is None:
                if self.min:
                    self.min=min(self.min,acc)
                else:
                    self.min=acc
                return
            if node.left:
                depth(node.left,acc+1)
            if node.right:
                depth(node.right,acc+1)
        depth(root,1)
        return self.min

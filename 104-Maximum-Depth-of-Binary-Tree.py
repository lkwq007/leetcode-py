# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.max=0
        def depth(node,acc):
            if node is None:
                self.max=max(self.max,acc)
                return
            depth(node.left,acc+1)
            depth(node.right,acc+1)
        depth(root,0)
        return self.max
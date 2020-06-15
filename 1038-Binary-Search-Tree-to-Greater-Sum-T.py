# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # do reverse inroder
        def dfs(node,acc):
            if node.right:
                dfs(node.right,acc)
            node.val+=acc[0]
            acc[0]=node.val
            if node.left:
                dfs(node.left,acc)
        dfs(root,[0])
        return root
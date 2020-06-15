# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node):
            if node.left is None and node.right is None:
                return node.val,0
            left=(0,0)
            right=(0,0)
            if node.left:
                left=dfs(node.left)
            if node.right:
                right=dfs(node.right)
            rob_this=node.val+left[1]+right[1]
            not_rob_this=max(left[0]+right[0],left[0]+right[1],left[1]+right[0],left[1]+right[1])
            return rob_this,not_rob_this
        return max(dfs(root))
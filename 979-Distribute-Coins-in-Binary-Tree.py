# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node):
            left=(0,0)
            right=(0,0)
            if node.left:
                left=dfs(node.left)
            if node.right:
                right=dfs(node.right)
            acc=left[1]+abs(left[0])+right[1]+abs(right[0])
            total=left[0]+right[0]+node.val
            return total-1,acc
        return dfs(root)[1]                                
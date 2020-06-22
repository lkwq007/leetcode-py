# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root is None:
            return root
        def dfs(node,acc):
            if node.left is None and node.right is None:
                acc+=node.val
                if acc>=limit:
                    return False
                return True
            left,right=True,True
            if node.left:
                left=dfs(node.left,node.val+acc)
                if left:
                    node.left=None
            if node.right:
                right=dfs(node.right,node.val+acc)
                if right:
                    node.right=None
            return left and right
        ret=dfs(root,0)
        return None if ret else root
                
            
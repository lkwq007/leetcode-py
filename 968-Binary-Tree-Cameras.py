# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node):
            if node.left is None and node.right is None:
                return 1,0
            left=[0,0]
            right=[0,0]
            if node.left:
                left=dfs(node.left)
            if node.right:
                right=dfs(node.right)
            # first is covered, second in not covered
            uncovered=left[0]+right[0]
            covered=min(left[1]+right[1]+1,left[0]+right[1]+1,left[1]+right[0]+1)
            return covered,uncovered
        ret,_=dfs(root)
        return ret

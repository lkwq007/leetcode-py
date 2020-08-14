# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        if root.val<L:
            return self.trimBST(root.right,L,R)
        elif root.val>R:
            return self.trimBST(root.left,L,R)
        root.left=self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)
        return root
        
        
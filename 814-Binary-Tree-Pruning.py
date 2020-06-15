# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        def prune(node):
            flag=node.val==1
            if node.left:
                tmp=prune(node.left)
                if not tmp:
                    node.left=None
                flag=tmp or flag
            if node.right:
                tmp=prune(node.right)
                if not tmp:
                    node.right=None
                flag=tmp or flag
            return flag
        ret=prune(root)
        return root if ret else None
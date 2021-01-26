# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def search(node,val):
            if node is None:
                return False
            if node.val==val:
                return True
            elif val>node.val:
                return search(node.right,val)
            else:
                return search(node.left,val)
        def dfs(node):
            if node is None:
                return False
            rest=k-node.val
            if rest<node.val:
                if search(node.left,rest):
                    return True
            elif rest>node.val:
                if search(root,rest):
                    return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
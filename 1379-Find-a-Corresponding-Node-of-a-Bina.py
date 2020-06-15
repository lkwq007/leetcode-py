# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node1,node2):
            if node1==target:
                return node2
            if node1 is None:
                return None
            ret=dfs(node1.left,node2.left)
            ret=ret if ret else dfs(node1.right,node2.right)
            return ret
        return dfs(original,cloned)
            
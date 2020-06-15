# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def compare(node1,node2):
            if node1 and node2:
                if node1.val==node2.val:
                    return compare(node1.left,node2.right) and compare(node1.right,node2.left)
                else:
                    return False
            else:
                return node1==node2
        return compare(root.left,root.right)
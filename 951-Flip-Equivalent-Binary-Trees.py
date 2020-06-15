# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def compare(node1,node2):
            if node1 and node2:
                if node1.val==node2.val:
                    ret=compare(node1.left,node2.left) and compare(node1.right,node2.right)
                    return ret or (compare(node1.right,node2.left) and compare(node1.left,node2.right))
                else:
                    return False
            else:
                return node1==node2
        return compare(root1,root2)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def compare(a,b):
            if a and b:
                if a.val==b.val:
                    return compare(a.left,b.left) and compare(a.right,b.right)
                else:
                    return False
            else:
                return a==b
        return compare(p,q)
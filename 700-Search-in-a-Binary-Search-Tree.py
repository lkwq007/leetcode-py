# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        node=root
        while node:
            if node.val==val:
                return node
            if node.val<val:
                node=node.right
            else:
                node=node.left
        return node
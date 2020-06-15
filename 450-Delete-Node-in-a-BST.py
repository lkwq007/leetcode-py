# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        node=root
        parent=None
        while node:
            if node.val==key:
                break
            elif node.val<key:
                parent=node
                node=node.right
            else:
                parent=node
                node=node.left
        if node is None:
            return root
        if node.right:
            tmp=node.right
            ptr=node.right
            left=node.left
            while ptr.left:
                ptr=ptr.left
            ptr.left=left
        else:
            tmp=node.left
        if parent:
            if parent.left==node:
                parent.left=tmp
            else:
                parent.right=tmp
        else:
            root=tmp
        return root

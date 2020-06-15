# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def search(node,ptr):
            if ptr is None:
                return True
            if node is None:
                return False
            if node.val==ptr.val:
                return search(node.left,ptr.next) or search(node.right,ptr.next)
            return False
        def dfs(node):
            ret=False
            if node:
                if node.val==head.val:
                    ret=search(node,head)
                if not ret:
                    ret=dfs(node.left) or dfs(node.right)
                return ret
            else:
                return False
        return dfs(root)

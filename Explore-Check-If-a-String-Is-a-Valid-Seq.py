# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root and arr and root.val==arr[0]:
            if root.left==None and root.right==None and len(arr)==1:
                return True
            return self.isValidSequence(root.left,arr[1:]) or self.isValidSequence(root.right,arr[1:])
        return False
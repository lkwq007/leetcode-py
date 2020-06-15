# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret=[]
        if root is None:
            return ret
        stack=[root]
        while stack:
            node=stack.pop()
            if type(node)==int:
                ret.append(node)
                continue
            stack.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ret
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node,min_val,max_val):
            if node is None:
                return 0
            min_val=min(node.val,min_val)
            max_val=max(node.val,max_val)
            return max(max_val-min_val,dfs(node.left,min_val,max_val),dfs(node.right,min_val,max_val))
        return dfs(root,root.val,root.val) if root else 0

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # stack can be removed
        if root is None:
            return 0
        self.max_diff=0
        self.min_stack=[root.val]
        self.max_stack=[root.val]
        def dfs(node):
            min_val=min(node.val,self.min_stack[-1])
            max_val=max(node.val,self.max_stack[-1])
            self.max_diff=max(self.max_diff,max_val-min_val)
            self.min_stack.append(min_val)
            self.max_stack.append(max_val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.min_stack.pop()
            self.max_stack.pop()
        dfs(root)
        return self.max_diff
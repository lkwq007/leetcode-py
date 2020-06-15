# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root.left:
            min_val=abs(root.left.val-root.val)
        else:
            min_val=abs(root.right.val-root.val)
        stack=[(root,False)]
        last=None
        while stack:
            node,flag=stack.pop()
            if flag:
                if last:
                    min_val=min(min_val,abs(node.val-last.val))
                last=node
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        return min_val

# remember this wrong answer
# [90,69,null,49,89,null,52,null,null,null,null]
# the largest value in the subtree is not the root of this subtree!
# class Solution:
#     def getMinimumDifference(self, root: TreeNode) -> int:
#         if root.left:
#             self.min=abs(root.val-root.left.val)
#         if root.right:
#             self.min=abs(root.val-root.right.val)
#         def dfs(node):
#             if node.left:
#                 left=abs(node.val-node.left.val)
#                 self.min=min(left,self.min)
#                 dfs(node.left)
#             if node.right:
#                 right=abs(node.val-node.right.val)
#                 self.min=min(right,self.min)
#                 dfs(node.right)
#         dfs(root)
#         return self.min
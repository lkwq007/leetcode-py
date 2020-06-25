# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max=0
        def dfs(node):
            left=(True,0)
            right=(True,0)
            left_min=node.val
            right_max=node.val
            if node.left:
                flag,total,left_min,left_max=dfs(node.left)
                left=(flag and node.val>left_max,total)
            if node.right:
                flag,total,right_min,right_max=dfs(node.right)
                right=(flag and node.val<right_min,total)
            if left[0] and right[0]:
                self.max=max(self.max,node.val+left[1]+right[1])
            return left[0] and right[0],node.val+left[1]+right[1],left_min,right_max
        dfs(root)
        return self.max
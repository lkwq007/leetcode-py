# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max=0
        def dfs(node):
            val=node.val
            if node.left:
                left,left_cnt=dfs(node.left)
            else:
                left=None
                left_cnt=0
            if node.right:
                right,right_cnt=dfs(node.right)
            else:
                right=None
                right_cnt=0
            ret=1
            if left==val:
                self.max=max(self.max,left_cnt)
                ret=max(ret,left_cnt+1)
            if right==val:
                self.max=max(self.max,right_cnt)
                ret=max(ret,right_cnt+1)
            if left==val==right:
                self.max=max(self.max,left_cnt+right_cnt)
            return val,ret
        dfs(root)
        return self.max
            
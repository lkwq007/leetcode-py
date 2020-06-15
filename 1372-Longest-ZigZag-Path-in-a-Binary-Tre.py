# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max=0
        def left(node):
            
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max=0
        def zigzag(node,flag):
            cnt=0
            tmp=node
            while tmp:
                cnt+=1
                if flag:
                    tmp.left_done=True
                else:
                    tmp.right_done=True
                tmp=tmp.left if flag else tmp.right
                flag=not flag
            self.max=max(self.max,cnt-1)
        def dfs(node):
            if not hasattr(node,"left_done"):
                zigzag(node,True)
            if not hasattr(node,"right_done"):
                zigzag(node,False)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.max
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        # two pass
        self.cnt=0
        self.max_depth=-1
        self.last=None
        def find_depth(node,depth):
            if node.left is None and node.right is None:
                if depth>self.max_depth:
                    self.max_depth=depth
                    self.cnt=1
                    self.last=node
                elif depth==self.max_depth:
                    self.cnt+=1
            if node.left:
                find_depth(node.left,depth+1)
            if node.right:
                find_depth(node.right,depth+1)
        find_depth(root,0)
        if self.cnt==1:
            return self.last
        self.ret=None
        def dfs(node,depth):
            if depth==self.max_depth:
                return 1
            ret=0
            if node.left:
                ret+=dfs(node.left,depth+1)
            if node.right:
                ret+=dfs(node.right,depth+1)
            if ret==self.cnt and self.ret is None:
                self.ret=node
                return 0
            return ret
        dfs(root,0)
        return self.ret
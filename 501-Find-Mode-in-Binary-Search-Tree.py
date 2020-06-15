# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.last=None
        self.cnt=1
        self.max_freq=1
        def inorder(node):
            if node.left:
                inorder(node.left)
            if node.val==self.last:
                self.cnt+=1
                self.max_freq=max(self.cnt,self.max_freq)
            else:
                self.last=node.val
                self.cnt=1
            if node.right:
                inorder(node.right)
        inorder(root)
        self.ret=[]
        self.last=None
        self.cnt=1
        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.val==self.last:
                self.cnt+=1
            else:
                self.last=node.val
                self.cnt=1
            if self.cnt==self.max_freq:
                self.ret.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.ret
# class Solution:
#     def findMode(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []
#         self.record={}
#         self.max_freq=1
#         def dfs(node):
#             val=node.val
#             if val in self.record:
#                 self.record[val]+=1
#                 self.max_freq=max(self.max_freq,self.record[val])
#             else:
#                 self.record[val]=1
#             if node.left:
#                 dfs(node.left)
#             if node.right:
#                 dfs(node.right)
#         dfs(root)
#         ret=[]
#         for key,val in self.record.items():
#             if val==self.max_freq:
#                 ret.append(key)
#         return ret
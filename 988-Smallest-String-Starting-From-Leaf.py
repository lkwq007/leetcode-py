# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root is None:
            return ""
        self.ret=None
        def dfs(node,lst):
            lst.append(node.val)
            if node.left is None and node.right is None:
                tmp=lst[::-1]
                if self.ret is None or tmp<self.ret:
                    self.ret=tmp
                lst.pop()
                return
            if node.left:
                dfs(node.left,lst)
            if node.right:
                dfs(node.right,lst)
            lst.pop()
        base=ord("a")
        dfs(root,[])
        return "".join(map(lambda x:chr(base+x),self.ret))
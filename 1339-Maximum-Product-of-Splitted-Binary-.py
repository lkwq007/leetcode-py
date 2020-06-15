# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node):
            if node is None:
                return 0
            return node.val+dfs(node.left)+dfs(node.right)
        total=dfs(root)
        term=10**9+7
        self.max=0
        def max_product(node):
            if node is None:
                return 0
            cur=node.val+max_product(node.left)+max_product(node.right)
            a=cur%term
            b=(total-cur)%term
            self.max=max(self.max,cur*(total-cur))
            return cur
        max_product(root)
        return self.max%term

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node):
            if node is None:
                return 0
            return node.val+dfs(node.left)+dfs(node.right)
        total=dfs(root)
        term=10**9+7
        self.max=[0,0,0]
        def max_product(node):
            if node is None:
                return 0
            cur=node.val+max_product(node.left)+max_product(node.right)
            a=(cur//term,cur%term)
            b=((total-cur)//term,(total-cur)%term)
            val=[a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[1]*b[1]]
            if val>self.max:
                self.max=val
            return cur
        max_product(root)
        return self.max[-1]%term
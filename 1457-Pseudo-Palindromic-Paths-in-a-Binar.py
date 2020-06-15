# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.record={}
        for idx in range(1,10):
            self.record[idx]=0
        self.cnt=0
        def dfs(node):
            self.record[node.val]+=1
            if node.left is None and node.right is None:
                even=0
                odd=0
                for key,val in self.record.items():
                    if val%2==1:
                        odd+=1
                    else:
                        even+=1
                if odd<2:
                    self.cnt+=1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.record[node.val]-=1
        dfs(root)
        return self.cnt
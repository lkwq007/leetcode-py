# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []
        to_delete_map={}
        for item in to_delete:
            to_delete_map[item]=1
        # each node in the tree has a distinct value.
        self.ret=[root]
        def dfs(node):
            if node.val in to_delete_map:
                del to_delete_map[node.val]
                if node.left:
                    self.ret.append(node.left)
                if node.right:
                    self.ret.append(node.right)
                return True
            if node.left:
                ret=dfs(node.left)
                if ret:
                    node.left=None
            if node.right:
                ret=dfs(node.right)
                if ret:
                    node.right=None
        idx=0
        while to_delete_map:
            node=self.ret[idx]
            ret=dfs(node)
            if ret:
                self.ret[idx]=None
            idx+=1
        return list(filter(lambda x:x,self.ret))
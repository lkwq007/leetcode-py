# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        def dfs(node):
            if node.left:
                node.left.val=2*node.val+1
                dfs(node.left)
            if node.right:
                node.right.val=2*node.val+2
                dfs(node.right)
        if root:
            root.val=0
            dfs(root)
        self.root=root

    def find(self, target: int) -> bool:
        if self.root is None:
            return False
        if target==0:
            return True
        stack=[]
        val=target
        while val>0:
            tmp=val%2
            stack.append(tmp)
            val=(val-1)>>1
        node=self.root
        while stack and node:
            if node.val==target:
                return True
            d=stack.pop()
            if d:
                node=node.left
            else:
                node=node.right
        if node is None:
            return False
        elif node.val==target:
            return True
        return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
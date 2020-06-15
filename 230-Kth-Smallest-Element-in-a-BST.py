# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt=0
        stack=[]
        node=root
        while True:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            cnt+=1
            if cnt==k:
                return node.val
            node=node.right
        return 0 

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack=[(root,False)]
        while stack:
            node,flag=stack.pop()
            if flag:
                k-=1
                if k==0:
                    return node.val
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        return 0 

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt=0
        if root is None:
            return 0
        stack=[(root,False)]
        while stack:
            node,flag=stack.pop()
            if flag:
                cnt+=1
                if k==cnt:
                    return node.val
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        return 0 
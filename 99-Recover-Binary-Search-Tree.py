# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None or (root.left is None and root.right is None):
            return
        lst=[]
        stack=[(root,False)]
        while stack:
            node,flag=stack.pop()
            if flag:
                lst.append(node)
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        total=len(lst)-1
        idx=0
        first=-1
        second=-1
        while idx<total:
            if lst[idx].val>lst[idx+1].val:
                if first>=0:
                    second=idx
                else:
                    first=idx
            idx+=1
        if second==-1:
            tmp=lst[first].val
            lst[first].val=lst[first+1].val
            lst[first+1].val=tmp
        else:
            tmp=lst[first].val
            lst[first].val=lst[second+1].val
            lst[second+1].val=tmp
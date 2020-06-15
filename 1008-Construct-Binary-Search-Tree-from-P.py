# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder)<1:
            return None
        def construct(lst):
            val=lst[0]
            root=TreeNode(val)
            idx=1
            total=len(lst)
            while idx<total:
                if lst[idx]>val:
                    break
                idx+=1            
            if idx>1:
                root.left=construct(lst[1:idx])
            if idx<len(lst):
                root.right=construct(lst[idx:])
            return root
        return construct(preorder)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder)<1:
            return None
        # note that it's a bst
        root=TreeNode(preorder[0])
        node=root
        stack=[root]
        idx=1
        total=len(preorder)
        while idx<total:
            val=preorder[idx]
            idx+=1
            tmp=TreeNode(val)
            if val<node.val:
                node.left=tmp
                stack.append(node)
                node=tmp
            else:
                last=node
                while stack:
                    last=node
                    node=stack.pop()
                    if val<node.val:
                        break
                last.right=tmp
                node=tmp
        return root
            
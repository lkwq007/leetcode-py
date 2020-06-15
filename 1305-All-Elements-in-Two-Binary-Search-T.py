# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack=[[(root1,False)] if root1 else [],[(root2,False)] if root2 else []]
        ret=[]
        def inorder(s):
            print(s)
            while s:
                node,flag=s.pop()
                if node is None:
                    continue
                if flag:
                    ret.append(node.val)
                    continue
                if node.right:
                    s.append((node.right,False))
                s.append((node,True))
                if node.left:
                    s.append((node.left,False))
        def update(s):
            node,flag=s.pop()
            if node is None:
                return
            if flag:
                s.append((node,flag))
                return
            if node.right:
                s.append((node.right,False))
            s.append((node,True))
            if node.left:
                s.append((node.left,False))
        while len(stack[0]) and len(stack[1]):
            cur=0
            while stack[0] and not stack[0][-1][1]:
                update(stack[0])
            while stack[1] and not stack[1][-1][1]:
                update(stack[1])
            if stack[0][-1][0].val<stack[1][-1][0].val:
                idx=0
            else:
                idx=1
            node,flag=stack[idx].pop()
            ret.append(node.val)
        if stack[0]:
            inorder(stack[0])
        else:
            inorder(stack[1])
        return ret
    
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack=[(root,0,0,0)]
        ret=0
        max_val=root.val
        while stack:
            node,state,left,right=stack.pop()
            if state==0:
                if node.left:
                    stack.append((node,1,left,right))
                    stack.append((node.left,0,0,0))
                else:
                    stack.append((node,1,left,right))
                    ret=None
            elif state==1:
                if ret:
                    left=ret
                    max_val=max(max_val,left)
                else:
                    left=0
                if node.right:
                    stack.append((node,2,left,right))
                    stack.append((node.right,0,0,0))
                else:
                    stack.append((node,2,left,right))
                    ret=None
            elif state==2:
                if ret:
                    right=ret
                    max_val=max(max_val,right)
                else:
                    right=0
                val=node.val
                max_val=max(max_val,left+val,right+val,left+right+val)
                ret=max(val,val+left,val+right)
        return max_val


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max=root.val
        def probe(node):
            val=node.val
            if node.left:
                left=probe(node.left)
                self.max=max(self.max,left)
            else:
                left=0
            if node.right:
                right=probe(node.right)
                self.max=max(self.max,right)
            else:
                right=0
            self.max=max(self.max,val,left+val,right+val,left+right+val)
            return max(val,val+left,val+right)
        probe(root)
        return self.max
x=Solution()
print(x.maxPathSum(TreeNode(-3)))
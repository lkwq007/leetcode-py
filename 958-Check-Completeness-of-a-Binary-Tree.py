# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # do level traversal
        if root is None:
            return True
        queue=[(root,0)]
        cur=-1
        idx=0
        cnt=0
        flag=False
        while idx<len(queue):
            node,depth=queue[idx]
            idx+=1
            if cur!=depth:
                cur=depth
                if flag:
                    cnt+=1
                flag=False
            if flag and node:
                return False
            if node is None:
                flag=True
            else:
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        if flag:
            cnt+=1
        return cnt<2

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # we can check this tree by checking the depth
        self.ret=True
        def depth(node,acc):
            left=(acc,acc)
            right=(acc,acc)
            if node.left and self.ret:
                left=depth(node.left,acc+1)
            if node.right and self.ret:
                right=depth(node.right,acc+1)
            # atmost one difference
            if left[0]!=left[1] and right[0]!=right[1]:
                self.ret=False
            elif left[0]<right[1]:
                self.ret=False
            return min(left[0],right[0]),max(left[1],right[1])
        a,b=depth(root,0)
        return self.ret and (b-a)<2
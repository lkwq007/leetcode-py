# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue=[(root,True)]
        idx=0
        last_level=False
        last_val=0
        while idx<len(queue):
            node,even_level=queue[idx]
            idx+=1
            if last_level!=even_level:
                last_level=even_level
                last_val=node.val-2 if even_level else node.val+2
            if even_level:
                if not (node.val&1 and node.val>last_val):
                    return False
            else:
                if not (node.val&1==0 and node.val<last_val):
                    return False
            last_val=node.val
            if node.left:
                queue.append((node.left,not even_level))
            if node.right:
                queue.append((node.right,not even_level))
        return True
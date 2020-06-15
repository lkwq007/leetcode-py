# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        left_queue=[root]
        left_idx=0
        right_queue=[]
        right_idx=0
        current=0
        ret=[]
        while left_idx<len(left_queue) or right_idx<len(right_queue):
            left=[]
            while left_idx<len(left_queue):
                node=left_queue[left_idx]
                left_idx+=1
                if node is not None:
                    left.append(node.val)
                    right_queue.append(node.left)
                    right_queue.append(node.right)
            if len(left)>0:
                ret.append(left)
            right=[]
            while right_idx<len(right_queue):
                node=right_queue[right_idx]
                right_idx+=1
                if node is not None:
                    right.append(node.val)
                    left_queue.append(node.left)
                    left_queue.append(node.right)
            if len(right)>0:
                ret.append(reversed(right))
        return ret
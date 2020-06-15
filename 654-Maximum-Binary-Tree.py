# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def search(lst):
            max_idx=0
            for idx in range(0,len(lst)):
                if lst[idx]>lst[max_idx]:
                    max_idx=idx
            return max_idx
        def construct(lst):
            if len(lst)<1:
                return None
            max_idx=search(lst)
            node=TreeNode(lst[max_idx])
            node.left=construct(lst[:max_idx])
            node.right=construct(lst[(max_idx+1):])
            return node
        return construct(nums)
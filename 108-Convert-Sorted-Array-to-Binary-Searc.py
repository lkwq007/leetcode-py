# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums)<1:
            return None
        def construct(lst):
            total=len(lst)
            if total<1:
                return None
            middle=total//2
            node=TreeNode(lst[middle])
            if middle<total:
                node.right=construct(lst[(middle+1):])
            if middle>0:
                node.left=construct(lst[0:middle])
            return node
        return construct(nums)
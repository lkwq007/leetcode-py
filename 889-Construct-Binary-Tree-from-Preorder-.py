# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre)<1 or len(post)<1:
            return None
        # distinct postive values
        total=len(pre)
        parent={}
        dummy_root=TreeNode(-1)
        ptr1=0
        ptr2=0
        last=dummy_root
        while True:
            while ptr1<total and ptr2<total and pre[ptr1]!=post[ptr2]:
                parent[pre[ptr1]]=last
                last=TreeNode(pre[ptr1])
                ptr1+=1
            if ptr1+1<total and ptr2+1<total and pre[ptr1+1]==post[ptr2+1]:
                

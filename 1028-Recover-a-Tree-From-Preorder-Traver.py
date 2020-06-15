# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        total=len(S)
        start=0
        end=0
        while end<total:
            if S[end]=="-":
                break
            end+=1
        root=TreeNode(int(S[0:end]))
        node=root
        stack=[(root,0)]
        depth=0
        start=end
        while end<total:
            cnt=0
            while S[end]=="-":
                cnt+=1
                end+=1
            start=end
            while end<total and S[end]!="-":
                end+=1
            val=int(S[start:end])
            start=end
            tmp=TreeNode(val)
            if cnt>depth:
                stack.append((node,depth))
                node.left=tmp
                depth=cnt
                node=tmp
            else:
                while stack:
                    node,depth=stack.pop()
                    if depth==cnt-1:
                        break
                node.right=tmp
                node=tmp
                stack.append((node,cnt))
        return root
                
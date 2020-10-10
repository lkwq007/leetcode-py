# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def encode(node):
            if node is None:
                return "n"
            left=encode(node.left)
            right=encode(node.right)
            return f"{node.val}({left})({right})"
        return encode(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data=="n":
            return None
        self.idx=0
        def decode(s):
            if s[self.idx]=="n":
                self.idx+=1
                node=None
            else:
                start=self.idx
                while self.idx<len(data) and s[self.idx]!="(":
                    self.idx+=1
                val=int(s[start:self.idx])
                node=TreeNode(val)
                if self.idx<len(data) and s[self.idx]=="(":
                    self.idx+=1
                    node.left=decode(s)
                if self.idx<len(data) and s[self.idx]=="(":
                    self.idx+=1
                    node.right=decode(s)
            if self.idx<len(data) and data[self.idx]==")":
                self.idx+=1
            return node
        root=decode(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
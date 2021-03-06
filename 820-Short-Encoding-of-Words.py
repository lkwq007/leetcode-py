class Node:
    def __init__(self):
        self.child={}
        self.end=False
# tire
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root=Node()
        for word in words:
            node=root
            for item in reversed(word):
                if item not in node.child:
                    node.child[item]=Node()
                node=node.child[item]
            node.end=True
        self.ret=0
        def dfs(node,acc):
            if node.end and len(node.child)==0:
                self.ret+=acc+1
            for next in node.child:
                dfs(node.child[next],acc+1)
        dfs(root,0)
        return self.ret
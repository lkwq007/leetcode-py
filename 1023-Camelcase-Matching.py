class Node:
    def __init__(self):
        self.children={}
        self.endpoint=False

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        root=Node()
        node=root
        for item in pattern:
            if item not in node.children:
                node.children[item]=Node()
            node=node.children[item]
        node.endpoint=True
        def check(word):
            node=root
            for item in word:
                if item.isupper():
                    if item not in node.children:
                        return False
                    else:
                        node=node.children[item]
                else:
                    if item not in node.children:
                        continue
                    else:
                        node=node.children[item]
            return node.endpoint
        return [check(word) for word in queries]

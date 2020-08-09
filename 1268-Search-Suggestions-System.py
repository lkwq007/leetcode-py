class Node:
    def __init__(self):
        self.children={}
        self.endpoint=False
        self.words=[]
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root=Node()
        def insert(word):
            node=root
            for item in word:
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
                node.words.append(word)
            node.endpoint=True
        for item in products:
            insert(item)
        node=root
        ret=[]
        flag=True
        for item in searchWord:
            if flag and item in node.children:
                node=node.children[item]
                node.words.sort()
                ret.append(node.words[:3])
            else:
                ret.append([])
                flag=False
        return ret
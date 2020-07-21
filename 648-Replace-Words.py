class Node:
    def __init__(self):
        self.endpoint=False
        self.children={}

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        root=Node()
        def insert(word):
            node=root
            for item in word:
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
            node.endpoint=True
        for item in dict:
            insert(item)
        words=sentence.split()
        def search(word):
            ret=""
            node=root
            for item in word:
                if item in node.children:
                    node=node.children[item]
                    ret+=item
                    if node.endpoint:
                        return ret
                else:
                    return word
            return ret
        for i in range(len(words)):
            words[i]=search(words[i])
        return " ".join(words)

class Node:
    def __init__(self):
        self.endpoint=False
        self.children={}

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # naive impl
        self.root=Node()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            node=self.root
            for item in word:
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
            node.endpoint=True
    
    def probe(self,word,node,modified):
        if not word:
            return node.endpoint and modified
        if modified:
            for item in word:
                if item in node.children:
                    node=node.children[item]
                else:
                    return False
            return node.endpoint
        else:
            item=word[0]
            next=word[1:]
            for key in node.children:
                if key==item:
                    if self.probe(next,node.children[key],False):
                        return True
                else:
                    if self.probe(next,node.children[key],True):
                        return True
        return False

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return self.probe(word,self.root,False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
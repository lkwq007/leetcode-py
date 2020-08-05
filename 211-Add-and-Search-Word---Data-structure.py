class Node:
    def __init__(self):
        self.children={}
        self.endpoint=False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node=self.root
        for item in word:
            if item not in node.children:
                node.children[item]=Node()
            node=node.children[item]
        node.endpoint=True
    
    def search_pos(self,node,word,i):
        while i<len(word):
            item=word[i]
            if item==".":
                for item in node.children:
                    if self.search_pos(node.children[item],word,i+1):
                        return True
                return False
            else:
                if item in node.children:
                    node=node.children[item]
                else:
                    return False
            i+=1
        return node.endpoint


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_pos(self.root,word,0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
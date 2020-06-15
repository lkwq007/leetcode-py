class TreeNode:
    def __init__(self,val):
        self.val=val
        self.leaf=False
        self.children={}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TreeNode(None)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.root
        for item in word:
            if item in node.children:
                node=node.children[item]
            else:
                tmp=TreeNode(item)
                node.children[item]=tmp
                node=tmp
        node.leaf=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.root
        for item in word:
            if item in node.children:
                node=node.children[item]
            else:
                return False
        return node.leaf

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.root
        for item in prefix:
            if item in node.children:
                node=node.children[item]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
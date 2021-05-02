class Node:
    def __init__(self):
        self.child={}
        self.flag=False
        self.val=[]
    
    def __repr__(self):
        return "{} {} ({})".format(self.flag,self.val,self.child)
class WordFilter:

    def __init__(self, words: List[str]):
        self.root=Node()
        def insert(word,idx):
            flag=False
            node=self.root
            for item in word:
                if item not in node.child:
                    node.child[item]=Node()
                node=node.child[item]
                if flag:
                    node.flag=True
                    node.val.append(idx)
                if item=="#":
                    flag=True
            # node.flag=True
            # node.val.append(idx)
        for idx,word in enumerate(words):
            for i in range(len(word)):
                cur=word[i:]+"#"+word
                insert(cur,idx)

    def f(self, prefix: str, suffix: str) -> int:
        val=suffix+"#"+prefix
        node=self.root
        for item in val:
            if item not in node.child:
                return -1
            node=node.child[item]
        if node.flag:
            return node.val[-1]
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
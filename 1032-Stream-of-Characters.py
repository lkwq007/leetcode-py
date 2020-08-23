class Node:
    def __init__(self):
        self.children={}
        self.endpoint=False


class StreamChecker:
    # TLE
    def __init__(self, words: List[str]):
        root=Node()
        for word in words:
            node=root
            for item in word:
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
            node.endpoint=True
        self.root=root
        self.set=set([])

    def query(self, letter: str) -> bool:
        current_set=set([])
        flag=False
        for node in self.set:
            if letter in node.children:
                tmp=node.children[letter]
                if tmp.endpoint:
                    flag=True
                current_set.add(tmp)
        if letter in self.root.children:
            current_set.add(self.root.children[letter])
            if self.root.children[letter].endpoint:
                flag=True
        self.set=current_set
        return flag
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
class Node:
    def __init__(self):
        self.children={}
        self.endpoint=False

class StreamChecker:
    # TLE
    def __init__(self, words: List[str]):
        root=Node()
        for word in words:
            node=root
            for item in word:
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
            node.endpoint=True
        self.root=root
        self.lst=[]

    def query(self, letter: str) -> bool:
        self.lst=[item.children[letter] for item in self.lst+[self.root] if letter in item.children]
        return any(item.endpoint for item in self.lst)

class Node:
    def __init__(self):
        self.children={}
        self.endpoint=False

class StreamChecker:
    def __init__(self, words: List[str]):
        root=Node()
        self.len=0
        for word in words:
            node=root
            self.len=max(self.len,len(words))
            for item in reversed(word):
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
            node.endpoint=True
        self.root=root
        self.buffer=""

    def query(self, letter: str) -> bool:
        self.buffer=(letter+self.buffer)[:self.len]
        node=self.root
        for item in self.buffer:
            if item in node.children:
                node=node.children[item]
                if node.endpoint:
                    return True
            else:
                return False
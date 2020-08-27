class Node:
    def __init__(self):
        self.children={}
        self.endpoint=True
        self.val=0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()
        

    def insert(self, key: str, val: int) -> None:
        node=self.root
        for item in key:
            if item not in node.children:
                node.children[item]=Node()
            node=node.children[item]
        node.endpoint=True
        node.val=val
    
    def dfs(self,node):
        ret=0
        stack=[node]
        while stack:
            top=stack.pop()
            if top.endpoint:
                ret+=top.val
            for _,val in top.children.items():
                stack.append(val)
        return ret

    def sum(self, prefix: str) -> int:
        node=self.root
        for item in prefix:
            if item in node.children:
                node=node.children[item]
            else:
                return 0
        return self.dfs(node)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

class Node:
    def __init__(self):
        self.children={}
        self.endpoint=True
        self.val=0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()
        self.mapping={}

    def insert(self, key: str, val: int) -> None:
        delta=val-self.mapping.get(key,0)
        self.mapping[key]=val
        node=self.root
        node.val+=delta
        for item in key:
            if item not in node.children:
                node.children[item]=Node()
            node=node.children[item]
            node.val+=delta
        node.endpoint=True

    def sum(self, prefix: str) -> int:
        node=self.root
        for item in prefix:
            if item in node.children:
                node=node.children[item]
            else:
                return 0
        return node.val
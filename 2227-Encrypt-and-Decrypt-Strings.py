class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.cnt=0
        self.child={}
        self.end=False

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d=dictionary
        self.keys=keys
        self.values=values
        self.mapping={}
        self.dict={}
        self.ret=0
        self.root=Node("")
        for i in range(len(dictionary)):
            self.dict[dictionary[i]]=i
        for k,v in zip(keys,values):
            self.mapping[k]=v
            if v not in self.mapping:
                self.mapping[v]=[]
            self.mapping[v].append(k)
        for word in dictionary:
            node_lst=[self.root]
            flag=True
            for c in word:
                if c not in self.mapping:
                    flag=False
                    break
                cur=self.mapping[c]
                lst=self.mapping[cur]
                target=set([])
                for node in node_lst:
                    for item0 in lst:
                        item=self.mapping[item0]
                        if item not in node.child:
                            tmp=Node(item)
                            node.child[item]=tmp
                        target.add(node.child[item])
                node_lst=list(target)
            if flag:
                for node in node_lst:
                    node.end=True
                    node.cnt+=1

    def encrypt(self, word1: str) -> str:
        ret=[]
        for item in word1:
            ret.append(self.mapping[item])
        return "".join(ret)

    def decrypt(self, word2: str) -> int:
        node=self.root
        for i in range(0,len(word2),2):
            item=word2[i:i+2]
            if item in node.child:
                node=node.child[item]
            else:
                return 0
        return node.cnt



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
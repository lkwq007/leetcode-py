class Node:
    def __init__(self):
        self.endpoint=False
        self.children={}
import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(s)<1 or len(wordDict)<1:
            return []
        root=Node()
        def insert(word):
            node=root
            for item in word:
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
            node.endpoint=True
        for word in wordDict:
            insert(word)
        @functools.lru_cache(maxsize=None)
        def probe(i,node):
            if i>=len(s):
                return [""]
            acc=""
            ret=[]
            while i<len(s) and s[i] in node.children:
                node=node.children[s[i]]
                acc+=s[i]
                if node.endpoint:
                    lst=probe(i+1,root)
                    for item in lst:
                        if item:
                            ret.append(acc+" "+item)
                        else:
                            ret.append(acc)
                i+=1
            return ret
        return probe(0,root)
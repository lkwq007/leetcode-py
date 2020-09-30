class Node:
    def __init__(self):
        self.children={}
        self.endpoint=False

import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root=Node()
        for word in wordDict:
            node=root
            for item in word:
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
            node.endpoint=True
        @functools.lru_cache(maxsize=None)
        def dfs(pos,node):
            if pos==len(s):
                return True
            while pos<len(s):
                if s[pos] in node.children:
                    node=node.children[s[pos]]
                    pos+=1
                    if node.endpoint:
                        if dfs(pos,root):
                            return True
                else:
                    break
            return False
        return dfs(0,root)
                
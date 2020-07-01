from typing import List
class Node:
    def __init__(self):
        self.endpoint=False
        self.children={}
        self.cache=None
    def __repr__(self):
        return str(self.children)+str(self.endpoint)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board)<1 or len(board[0])<1 or len(words)<1:
            return []
        root=Node()
        def insert(word):
            node=root
            for item in word:
                if item not in node.children:
                    node.children[item]=Node()
                node=node.children[item]
            node.endpoint=True
            node.cache=word
        def delete(word):
            node=root
            stack=[]
            for item in word:
                stack.append((node,item))
                node=node.children[item]
            if len(node.children)>0:
                node.endpoint=False
                node.cache=None
                return
            while stack:
                node,item=stack.pop()
                del node.children[item]
                if node.endpoint or len(node.children)>0:
                    return
        for word in words:
            insert(word)
        self.ret=[]
        h=len(board)
        w=len(board[0])
        direction=[[0,-1],[0,1],[-1,0],[1,0]]
        def dfs(y:int,x:int,node:Node):
            item=board[y][x] if y>=0 and x>=0 and y<h and x<w else "0"
            if item not in node.children:
                return False
            next=node.children[item]
            if next.endpoint:
                self.ret.append(next.cache)
                if len(next.children)>0:
                    next.endpoint=False
                else:
                    delete(next.cache)
                    return True
            ret=False
            board[y][x]="1"
            for y_offset,x_offset in direction:
                dfs(y+y_offset,x+x_offset,next)
            board[y][x]=item
            return ret
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] in root.children:
                    dfs(y,x,root)
        return self.ret

x=Solution()
print(x.findWords([["a","b"],["c","d"]],["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]))
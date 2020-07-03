from typing import List
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        # it's seem that this tree might not be a binary tree
        self.table={}
        total=len(parent)
        self.childs=[0]*total
        self.leaf=[0]*total
        self.depth=[0]*total
        for idx in range(1,total):
            par=parent[idx]
            self.childs[par]+=1
        def dfs(idx):
            tmp=idx
            lst=[]
            cnt=0
            while tmp!=-1:
                lst.append(tmp)
                if self.leaf[tmp]==0:
                    self.leaf[tmp]=idx
                    self.depth[tmp]=cnt
                cnt+=1
                tmp=parent[tmp]
            return lst
        for idx in range(0,total):
            if self.childs[idx]==0:
                par=parent[idx]
                lst=dfs(idx)
                self.leaf[idx]=idx
                self.table[idx]=lst

    def getKthAncestor(self, node: int, k: int) -> int:
        leaf=self.leaf[node]
        lst=self.table[leaf]
        depth=self.depth[node]
        if depth+k>=len(lst):
            return -1
        return lst[depth+k]

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[8,[-1,0,0,7,1,2,2,1]],[4,1],[5,2],[6,3]]

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        # it's seem that this tree might not be a binary tree
        self.table={}
        total=len(parent)
        self.childs=[0]*total
        self.leaf=[0]*total
        self.depth=[0]*total
        for idx in range(1,total):
            par=parent[idx]
            self.childs[par]+=1
        def dfs(idx):
            tmp=idx
            lst=[]
            cnt=0
            while tmp!=-1:
                lst.append(tmp)
                if self.leaf[tmp]==0:
                    self.leaf[tmp]=idx
                    self.depth[tmp]=cnt
                cnt+=1
                tmp=parent[tmp]
            return lst
        for idx in range(0,total):
            if self.childs[idx]==0:
                par=parent[idx]
                if self.leaf[par]==0:
                    lst=dfs(idx)
                else:
                    lst=self.table[self.leaf[par]]
                    self.depth[idx]=self.depth[par]-1
                self.leaf[idx]=idx
                self.table[idx]=lst

    def getKthAncestor(self, node: int, k: int) -> int:
        leaf=self.leaf[node]
        lst=self.table[leaf]
        depth=self.depth[node]
        if depth+k>=len(lst):
            return -1
        return lst[depth+k]
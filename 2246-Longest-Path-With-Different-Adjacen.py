class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.ret=1
        tree=[[] for _ in range(len(parent))]
        for i in range(1,len(parent)):
            tree[parent[i]].append(i)
        def dfs(x):
            lst=[0,0]
            def insert(val):
                if val>=lst[0]:
                    lst[1]=lst[0]
                    lst[0]=val
                elif val>=lst[1]:
                    lst[1]=val
            for child in tree[x]:
                below=dfs(child)
                if s[child]!=s[x]:
                    insert(below)
            self.ret=max(self.ret,1+lst[0]+lst[1])
            return 1+max(lst)
        dfs(0)
        return self.ret
        
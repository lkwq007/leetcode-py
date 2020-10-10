class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        ret=[]
        graph={}
        for i in range(len(beforeItems)):
            for u in beforeItems[i]:
                if u not in graph:
                    graph[u]=[]
                graph[u].append(i)
        tout=[-1]*n
        tin=[-1]*n
        visited=[False]*n
        self.timer=0
        lst=[]
        self.flag=False
        def dfs(u):
            tin[u]=self.timer
            self.timer+=1
            visited[u]=True
            if u in graph:
                for v in graph[u]:
                    if not visited[v]:
                        dfs(v)
                    elif tout[v]==-1:
                        self.flag=True
            tout[u]=self.timer
            self.timer+=1
            lst.append(u)
        for i in range(n):
            if not visited[i]:
                if i in graph:
                    dfs(i)
        if self.flag:
            return []
        lst=lst[::-1]
        record={}
        for i in range(n):
            if group[i] not in record:
                record[group[i]]=[]
            record[group[i]].append(i)
        ret=[]
        print(lst)
        for i in range(len(lst)):
            item=lst[i]
            if i==len(lst)-1 or group[lst[i]]!=group[lst[i+1]]:
                ret.append(item)
                if group[item]!=-1:
                    if group[item] not in record:
                        return []
                    for val in record[group[item]]:
                        if not visited[val]:
                            ret.append(val)
                    del record[group[item]]
            else:
                ret.append(item)
                visited[item]=True
        return ret
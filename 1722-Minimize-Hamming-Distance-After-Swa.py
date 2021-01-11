class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        visited=[0]*len(source)
        graph={}
        for a,b in allowedSwaps:
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            graph[a].append(b)
            graph[b].append(a)
        def dfs(idx,record):
            visited[idx]=1
            src=source[idx]
            tgt=target[idx]
            record[src]=record.get(src,0)+1
            record[tgt]=record.get(tgt,0)-1
            for next in graph.get(idx,[]):
                if visited[next]==0:
                    dfs(next,record)
        ret=0
        for i in range(len(source)):
            if visited[i]==0:
                tmp={}
                dfs(i,tmp)
                acc=0
                for k,v in tmp.items():
                    if v!=0:
                        acc+=abs(v)
                ret+=acc//2
        return ret
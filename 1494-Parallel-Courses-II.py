from typing import List
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # labeled 1->n 
        if n<2 or k<2:
            return n
        if len(dependencies)<1:
            if n%k==0:
                return n//k
            else:
                return n//k+1
        indegree=[0]*(n+1)
        depth=[0]*(n+1)
        graph={}
        for prereq,item in dependencies:
            indegree[item]+=1
            if prereq not in graph:
                graph[prereq]={}
            graph[prereq][item]=1
        taken=0
        step=0
        def dfs(node):
            if depth[node]>0:
                return depth[node]
            if node not in graph:
                depth[node]=1
                return 1
            max_val=1
            for next in graph[node]:
                ret=dfs(next)
                max_val=max(max_val,ret)
            depth[node]=max_val+1
            return max_val+1
        for idx in range(1,n+1):
            dfs(idx)
        def test(x):
            if x in graph:
                return min(map(lambda y:indegree[y],graph[x].keys()))*100+15-depth[x]
            else:
                return n*100+15-depth[x]
        while taken<n:
            target=[]
            for idx in range(1,n+1):
                if indegree[idx]==0:
                    target.append(idx)
            if len(target)<=k:
                total=len(target)
            else:
                target.sort(key=test)
                total=k
            for idx in range(total):
                item=target[idx]
                indegree[item]=-1
                if item in graph:
                    for next in graph[item]:
                        indegree[next]-=1
            print(target,target[:total])
            taken+=total
            step+=1
        return step

x=Solution()
print(x.minNumberOfSemesters(12,[[1,2],[2,3],[4,5],[5,6],[7,8],[8,9],[10,11],[11,12]],3))

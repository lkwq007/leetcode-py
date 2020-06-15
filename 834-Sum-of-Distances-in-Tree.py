from typing import List
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        root=0
        total=len(edges)+1
        parent=[0]*total
        ret=[0]*total
        connection=[None]*total
        child_cnt=[0]*total
        # An undirected, connected tree 
        for v0,v1 in edges:
            if connection[v0] is None:
                connection[v0]=[v1]
            else:
                connection[v0].append(v1)
            if connection[v1] is None:
                connection[v1]=[v0]
            else:
                connection[v1].append(v0)
        def dfs(node):
            children=connection[node]
            acc=0
            dist=[]
            if children:
                for item in children:
                    if connection[item]:
                        for idx in range(0,len(connection[item])):
                            if connection[item][idx]==node:
                                tmp=connection[item]
                                del tmp[idx]
                                break
                    cnt,lst=dfs(item)
                    acc+=cnt+1
                    dist.append(sum(lst)+cnt+1)
            child_cnt[node]=acc
            return acc,dist
        _,tmp=dfs(root)
        ret[root]=sum(tmp)
        def fill(node):
            total_child=child_cnt[node]
            if connection[node]:
                for item in connection[node]:
                    parent[item]=parent[node]+total_child-child_cnt[item]-1+1
                    ret[item]=ret[node]+parent[item]-1-child_cnt[item]
                    fill(item)
        fill(root)
        return ret

x=Solution()
print(x.sumOfDistancesInTree(6,[[0,1],[0,2],[2,3],[2,4],[2,5]]))
print(x.sumOfDistancesInTree(3,[[2,0],[1,0]]))

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # note that it's a acyclic graph, so we can just check indegree
        indegree=[0]*n
        for u,v in edges:
            indegree[v]+=1
        ret=[]
        for i in range(n):
            if indegree[i]==0:
                ret.append(i)
        return ret

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # note that it's a acyclic graph, so we can just check indegree
        indegree=[0]*n
        for u,v in edges:
            indegree[v]+=1
        ret=[]
        for i in range(n):
            if indegree[i]==0:
                ret.append(i)
        return ret
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topo sort
        indegree=[0]*numCourses
        graph={}
        for cur,preq in prerequisites:
            indegree[cur]+=1
            if preq in graph:
                graph[preq].append(cur)
            else:
                graph[preq]=[cur]
        queue=[]
        visited=[]
        total=0
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        target=[]
        while queue:
            for item in queue:
                visited.append(item)
                if item in graph:
                    for next in graph[item]:
                        indegree[next]-=1
                        if indegree[next]==0:
                            target.append(next)
            queue=target
            target=[]
        if len(visited)!=numCourses:
            return []
        return visited

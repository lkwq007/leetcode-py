from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        indegree=[0]*numCourses
        graph={}
        for cur,pre in prerequisites:
            if pre in graph:
                graph[pre].append(cur)
            else:
                graph[pre]=[cur]
            indegree[cur]+=1
        queue=[]
        for idx in range(len(indegree)):
            if indegree[idx]==0:
                queue.append(idx)
        idx=0
        while idx<len(queue):
            cur=queue[idx]
            idx+=1
            if cur in graph:
                for nextC in graph[cur]:
                    indegree[nextC]-=1
                    if indegree[nextC]==0:
                        queue.append(nextC)
        return idx==numCourses
x=Solution()
print(x.canFinish(2,[[1,0]]))

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses==1:
            return True
        record=[-1]*numCourses
        graph={}
        for cur,pre in prerequisites:
            if cur in graph:
                graph[cur].append(pre)
            else:
                graph[cur]=[pre]
        self.flag=True
        def dfs(idx):
            if record[idx]==1:
                return True
            elif record[idx]==0:
                self.flag=False
                return False
            else:
                record[idx]=0
                if idx in graph:
                    for item in graph[idx]:
                        if not dfs(item):
                            self.flag=False
                            return False
                record[idx]=1
            return True
        for idx in range(0,len(record)):
            if record[idx]==-1:
                dfs(idx)
                if not self.flag:
                    return False
        return True

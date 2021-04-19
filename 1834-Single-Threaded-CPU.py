import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        lst=[i for i in range(len(tasks))]
        lst.sort(key=lambda i:tasks[i][0])
        heap=[]
        heapq.heapify(heap)
        cur=tasks[lst[0]][0]
        idx=0
        ret=[]
        while len(ret)<len(tasks):
            while idx<len(lst) and (tasks[lst[idx]][0]<=cur or len(heap)==0):
                if len(heap)==0:
                    cur=max(cur,tasks[lst[idx]][0])
                heapq.heappush(heap,(tasks[lst[idx]][1],lst[idx]))
                idx+=1
            target=heapq.heappop(heap)
            ret.append(target[1])
            cur+=target[0]
        return ret
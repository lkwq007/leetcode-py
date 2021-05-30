import heapq
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        queue=[]
        heapq.heapify(queue)
        pool=[(servers[i],i) for i in range(len(servers))]
        heapq.heapify(pool)
        idx=0
        ret=[]
        for i in range(len(tasks)):
            while queue and queue[0][0]<=i:
                top=heapq.heappop(queue)
                heapq.heappush(pool,(top[1],top[2]))
            while idx<=i:
                if pool:
                    top=heapq.heappop(pool)
                    ret.append(top[1])
                    heapq.heappush(queue,(i+tasks[idx],top[0],top[1]))
                    idx+=1
                else:
                    break
        cur=len(tasks)
        while idx<len(tasks):
            if pool:
                top=heapq.heappop(pool)
                ret.append(top[1])
                heapq.heappush(queue,(cur+tasks[idx],top[0],top[1]))
                idx+=1
            if queue:
                top=heapq.heappop(queue)
                heapq.heappush(pool,(top[1],top[2]))
                cur=top[0]
        return ret
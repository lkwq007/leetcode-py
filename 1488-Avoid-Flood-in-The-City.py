from collections import deque
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        queue=deque([])
        ret=[-1]*len(rains)
        record={}
        for i in range(len(rains)):
            item=rains[i]
            if item==0:
                queue.append(i)
            else:
                if item not in record:
                    record[item]=i
                else:
                    lst=[]
                    while queue and queue[0]<record[item]:
                        idx=queue.popleft()
                        lst.append(idx)
                    if queue and queue[0]>record[item]:
                        idx=queue.popleft()
                        ret[idx]=item
                        record[item]=i
                        queue.extendleft(lst)
                    else:
                        return []
        while queue:
            top=queue.pop()
            ret[top]=1
        return ret
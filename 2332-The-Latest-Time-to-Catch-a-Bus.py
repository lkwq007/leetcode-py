class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        ret=0
        from collections import deque
        record={}
        passengers.sort()
        for item in passengers:
            if item-1 not in record:
                record[item]=item-1
            else:
                record[item]=record[item-1]
        lst=[(item,0) for item in passengers]+[(item,1) for item in buses]
        lst.sort()
        queue=deque([],maxlen=len(passengers))
        for item,t in lst:
            if t==1:
                if len(queue)<capacity:
                    ret=record.get(item,item)
                    for i in range(len(queue)):
                        queue.popleft()
                else:
                    for i in range(capacity):
                        head=queue.popleft()
                        ret=record.get(head-1,head-1)
            else:
                queue.append(item)
        return ret

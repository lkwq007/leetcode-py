class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        idx=0
        day=0
        ret=0
        buffer=[]
        while idx<len(events):
            item=events[idx]
            if day!=item[0]:
                day=item[0]
                ret+=1
                idx+=1
                while idx<len(events) and events[idx][0]==day:
                    if day!=events[idx][1]:
                        buffer.append(events[idx][1])
                    idx+=1
                if idx<len(events):
                    next=events[idx][0]
                else:
                    next=100001
                for item in buffer:
                    if day<next and day<=item:
                        day+=1
                        ret+=1
                
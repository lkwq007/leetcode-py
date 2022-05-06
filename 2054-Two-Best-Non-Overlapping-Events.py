class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ret=1
        events.sort(key=lambda x:(x[1],x[0],x[2]))
        lst=[0]*len(events)
        for i,item in enumerate(events):
            start,end,val=item
            left=0
            right=i
            while left<right:
                middle=left+(right-left)//2
                if events[middle][1]<start:
                    left=middle+1
                else:
                    right=middle
            while left>=0 and events[left][1]>=start:
                left-=1
            ret=max(val+lst[left],ret)
            lst[i]=max(val,lst[i-1])
        return ret

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ret=1
        events.sort()
        import heapq
        heap=[]
        acc=0
        for start,end,val in events:
            while heap and heap[0][0]<start:
                top=heapq.heappop(heap)
                acc=max(acc,top[1])
            ret=max(ret,acc+val)
            heapq.heappush(heap,(end,val))
        return ret
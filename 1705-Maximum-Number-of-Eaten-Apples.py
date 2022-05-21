import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap=[]
        mapping={}
        ret=0
        for i in range(len(apples)+max(days)):
            if i<len(apples):
                rot=i+days[i]-1
                if rot in mapping:
                    mapping[rot]+=apples[i]
                else:
                    mapping[rot]=apples[i]
                    heapq.heappush(heap,rot)
            while heap and (heap[0]<i or mapping[heap[0]]==0):
                heapq.heappop(heap)
            if heap and heap[0]>=i:
                ret+=1
                mapping[heap[0]]-=1
        return ret
                

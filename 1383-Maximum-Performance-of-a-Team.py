class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        term=10**9+7
        heap=[]
        lst=[i for i in range(n)]
        lst.sort(key=lambda x:(-efficiency[x],-speed[x]))
        ret=0
        acc=0
        for i in range(k):
            idx=lst[i]
            acc+=speed[idx]
            heap.append(speed[idx])
            ret=max(ret,acc*efficiency[idx])
        # build heap
        import heapq
        heapq.heapify(heap)
        for i in range(k,n):
            idx=lst[i]
            if heap[0]<speed[idx]:
                acc=acc-heap[0]+speed[idx]
                heapq.heapreplace(heap,speed[idx])
                ret=max(ret,acc*efficiency[idx])
        return ret%term
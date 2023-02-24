class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        import heapq
        lst=set()
        for item in nums:
            if item%2:
                lst.add(-item*2)
            else:
                lst.add(-item)
        heap=list(lst)
        min_val=-max(heap)
        heapq.heapify(heap)
        max_val=-heap[0]
        ret=max_val-min_val
        while heap:
            top=-heapq.heappop(heap)
            ret=min(ret,top-min_val)
            if top%2==0:
                tmp=top//2
                min_val=min(tmp,min_val)
                heapq.heappush(heap,-tmp)
            else:
                break
        return ret


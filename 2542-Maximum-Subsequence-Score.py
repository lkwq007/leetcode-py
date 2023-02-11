class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        lst=list(range(len(nums1)))
        lst.sort(key=lambda x:-nums2[x])
        import heapq
        heap=[]
        ret=0
        acc=0
        for i in range(k):
            idx=lst[i]
            heapq.heappush(heap,nums1[idx])
            acc+=nums1[idx]
        ret=acc*nums2[lst[k-1]]
        for i in range(k,len(lst)):
            idx=lst[i]
            item=nums1[idx]
            cur=nums2[idx]
            top=heap[0]
            if item>top:
                heapq.heappop(heap)
                heapq.heappush(heap,item)
                acc=acc-top+item
                ret=max(acc*cur,ret)
        return ret

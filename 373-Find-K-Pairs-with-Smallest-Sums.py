class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        queue=[(nums1[0]+nums2[0],0,0)]
        ret=[]
        record={}
        while k>0 and queue:
            val,idx1,idx2=heapq.heappop(queue)
            ret.append((nums1[idx1],nums2[idx2]))
            if idx2+1<len(nums2) and (idx1,idx2+1) not in record:
                heapq.heappush(queue,(nums1[idx1]+nums2[idx2+1],idx1,idx2+1))
                record[(idx1,idx2+1)]=1
            if idx1+1<len(nums1) and (idx1+1,idx2) not in record:
                heapq.heappush(queue,(nums1[idx1+1]+nums2[idx2],idx1+1,idx2))
                record[(idx1+1,idx2)]=1
            k-=1
        return ret

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        queue=[(nums1[0]+nums2[0],0,0)]
        ret=[]
        while k>0 and queue:
            val,idx1,idx2=heapq.heappop(queue)
            ret.append((nums1[idx1],nums2[idx2]))
            if idx2+1<len(nums2):
                heapq.heappush(queue,(nums1[idx1]+nums2[idx2+1],idx1,idx2+1))
            if idx2==0 and idx1+1<len(nums1):
                heapq.heappush(queue,(nums1[idx1+1]+nums2[idx2],idx1+1,idx2))
            k-=1
        return ret
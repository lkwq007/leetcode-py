from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K<1:
            return []
        if K>=len(points):
            return points
        def dist(point:List[int])->int:
            return point[0]*point[0]+point[1]*point[1]
        # max heap
        heap=[]
        for idx in range(0,K):
            heap.append(points[idx])
        def heapify(idx):
            tmp=idx
            left=2*idx+1
            right=2*idx+2
            if left<K and dist(heap[tmp])<dist(heap[left]):
                tmp=left
            if right<K and dist(heap[tmp])<dist(heap[right]):
                tmp=right
            if tmp!=idx:
                swap=heap[tmp]
                heap[tmp]=heap[idx]
                heap[idx]=swap
                heapify(tmp)
        for idx in range(K//2,-1,-1):
            heapify(idx)
        for idx in range(K,len(points)):
            if dist(points[idx])>=dist(heap[0]):
                continue
            else:
                heap[0]=points[idx]
                heapify(0)
        return heap
x=Solution()
x.kClosest([[3,3],[5,-1],[-2,4]],2)
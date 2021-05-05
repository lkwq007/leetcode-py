import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # greedy
        courses.sort(key=lambda x:(x[1],x[0]))
        heap=[]
        heapq.heapify(heap)
        cur=0
        for dur,due in courses:
            if cur+dur<=due:
                cur+=dur
                heapq.heappush(heap,-dur)
            elif heap:
                top=-heap[0]
                if top>dur:
                    cur=cur-top+dur
                    heapq.heapreplace(heap,-dur)
        return len(heap)
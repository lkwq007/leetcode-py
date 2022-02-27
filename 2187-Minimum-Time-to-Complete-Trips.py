class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left=min(time)
        right=left*totalTrips
        def check(t):
            acc=0
            for i in range(len(time)):
                acc+=t//time[i]
            return acc>=totalTrips
        while left<right:
            middle=left+(right-left)//2
            if check(middle):
                right=middle
            else:
                left=middle+1
        if check(left-1):
            return left-1
        return left



# import heapq
# class Solution:
#     def minimumTime(self, time: List[int], totalTrips: int) -> int:
#         # TLE
#         total=totalTrips
#         cur=0
#         heap=[]
#         record={}
#         for i in range(len(time)):
#             t=time[i]
#             if t not in record:
#                 record[t]=[]
#                 heapq.heappush(heap,t)
#             record[t].append(i)
#         while total>0:
#             cur=heapq.heappop(heap)
#             total-=len(record[cur])
#             for idx in record[cur]:
#                 t=cur+time[idx]
#                 if t not in record:
#                     record[t]=[]
#                     heapq.heappush(heap,t)
#                 record[t].append(idx)
#         return cur

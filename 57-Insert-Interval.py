class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # I got a simple idea
        # intervals is already sorted
        # *non-overlapping*
        def search(val,left=0):
            left=left
            right=2*len(intervals)
            while left<right:
                middle=left+(right-left)//2
                idx=middle//2
                end=middle&1
                if intervals[idx][end]==val:
                    return middle
                elif intervals[idx][end]<val:
                    left=middle+1
                else:
                    right=middle
            return left
        start=search(newInterval[0])
        end=search(newInterval[1],start)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # brute force
        ret=[]
        i=0
        flag=False
        while i<len(intervals):
            item=intervals[i]
            if item[1]<newInterval[0] or flag and item[0]>newInterval[1]:
                ret.append(item)
                i+=1
            elif item[0]<=newInterval[0]<=item[1]:
                start=min(newInterval[0],item[0])
                end=max(newInterval[1],item[1])
                while i<len(intervals) and intervals[i][0]<=end:
                    end=max(end,intervals[i][1])
                    i+=1
                ret.append([start,end])
                flag=True
            else:
                start=newInterval[0]
                end=newInterval[1]
                while i<len(intervals) and intervals[i][0]<=end:
                    end=max(end,intervals[i][1])
                    i+=1
                ret.append([start,end])
                flag=True
        return ret if flag else ret+[newInterval]

            

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         # intervals is already sorted
#         # *non-overlapping*
#         left=0
#         right=len(intervals)
#         while left<right:
#             middle=left+(right-left)//2
#             if intervals[middle][0]>newInterval[0]:
#                 right=middle-1
#             elif intervals[middle][0]==newInterval[0]:
#                 left=middle
#                 break
#             else:
#                 left=middle
#         start=left
#         if intervals[left][1]<newInterval[0]:
#             pass
#         left=left
#         right=len(intervals)
#         while left<right:
#             middle=left+(right-left)//2
#             if intervals[middle]:
#                 pass
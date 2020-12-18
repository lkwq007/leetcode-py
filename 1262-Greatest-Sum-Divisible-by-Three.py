from collections import deque
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # all positive
        nums.sort(key=lambda x:-x)
        ret=0
        queue1=deque([])
        queue2=deque([])
        queue=[queue1,queue2]
        for item in nums:
            if item%3==0:
                ret+=item
            else:
                idx=item%3-1
                if queue[1-idx]:
                    top=queue[1-idx].popleft()
                    ret+=item+top
                else:
                    queue[idx].append(item)
                if len(queue[idx])==3:
                    ret+=sum(queue[idx])
                    queue[idx].clear()
        return ret
                



# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         # all positive
#         ret=0
#         lst1=[]
#         lst2=[]
#         for item in nums:
#             if item%3==0:
#                 ret+=item
#             elif item%3==1:
#                 lst1.append(item)
#             else:
#                 lst2.append(item)
#         if len(lst1)>0 and len(lst2)>0:
#             lst1.sort(key=lambda x:-x)
#             lst2.sort(key=lambda x:-x)
#             total=min(len(lst1),len(lst2))
#             return sum(lst1[:total])+sum(lst2[:total])+ret
#         return ret

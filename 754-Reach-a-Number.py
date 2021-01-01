from math import sqrt
class Solution:
    def reachNumber(self, target: int) -> int:
        if target==0:
            return 0
        target=abs(target)
        x=(-1+sqrt(1+8*target))/2
        left=int(x)
        right=left+1
        def calc(x):
            return x*(1+x)//2
        if calc(left)==target:
            return left
        idx=right
        while True:
            total=calc(idx)
            if (total-target)%2==0:
                return idx
            idx+=1

x=Solution()
print(x.reachNumber(317231))

# NO, this is not BFS problem, this is a math problem
# class Solution:
#     def reachNumber(self, target: int) -> int:
#         if target==0:
#             return 0
#         record={0:0}
#         step=0
#         queue=[0]
#         while queue:
#             target_queue=[]
#             step+=1
#             for pos in queue:
#                 for next in (pos-step,pos+step):
#                     if next==target:
#                         return step
#                     record[next]=step
#                     target_queue.append(next)
#             queue=target_queue
#         return 0
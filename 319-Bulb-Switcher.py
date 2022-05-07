class Solution:
    def bulbSwitch(self, n: int) -> int:
        import math
        return int(math.sqrt(n))
# class Solution:
#     def bulbSwitch(self, n: int) -> int:
#         # brute force, TLE
#         if n==0:
#             return 0
#         def count(x):
#             cur=1
#             ret=0
#             while cur*cur<=x:
#                 if x%cur==0:
#                     ret+=1 if cur*cur==x else 2
#                 cur+=1
#             return ret
#         acc=0
#         for i in range(1,n+1):
#             if count(i)%2:
#                 acc+=1
#         return acc
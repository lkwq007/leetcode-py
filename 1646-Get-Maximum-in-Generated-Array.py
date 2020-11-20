# class Solution:
#     def getMaximumGenerated(self, n: int) -> int:
#         import functools
#         @functools.lru_cache(maxsize=None)
#         def calc(x):
#             if x<2:
#                 return x
#             if x&1:
#                 return calc(x//2)+calc(x//2+1)
#             else:
#                 return calc(x//2)
#         return max(calc(n),calc(n-1))
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<2:
            return n
        lst=[0]*(n+1)
        lst[1]=1
        ret=0
        for i in range(2,n+1):
            if i&1:
                lst[i]=lst[i//2]+lst[i//2+1]
            else:
                lst[i]=lst[i//2]
            ret=max(ret,lst[i])
        return ret

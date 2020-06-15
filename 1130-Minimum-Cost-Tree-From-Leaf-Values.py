# class Solution:
#     def mctFromLeafValues(self, arr: List[int]) -> int:
#         if len(arr)<1:
#             return 0
#         total=len(arr)
#         template=[0]*(total+1)
#         dp=[template[:] for _ in range(total+1)]
#         for offset in range(1,total-1):
#             for i in range(0,total-offset):
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr)<1:
            return 0
        total=len(arr)
        template=[0]*(total+1)
        dp=[template[:] for _ in range(total+1)]
        def 
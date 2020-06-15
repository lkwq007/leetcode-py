from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def max_sub(arr):
            ret=arr[0]
            acc=0
            for item in arr:
                acc=item+max(0,acc)
                ret=max(acc,ret)
            return ret
        # case 1
        max_val=max_sub(A)
        right_sum=[0]*len(A)
        right_sum[-1]=A[-1]
        for idx in range(-2,-len(A)-1,-1):
            right_sum[idx]=A[idx]+right_sum[idx+1]
        max_right=right_sum[:]
        for idx in range(-2,-len(A)-1,-1):
            max_right[idx]=max(max_right[idx],max_right[idx+1])
        left_sum=0
        for idx in range(0,len(A)-2):
            left_sum+=A[idx]
            max_val=max(max_val,left_sum+max_right[idx+2])
        return max_val
           
# WA
# class Solution:
#     def maxSubarraySumCircular(self, A: List[int]) -> int:
#         if len(A)<1:
#             return 0
#         if len(A)==1:
#             return A[0]
#         max_sum=A[0]
#         idx=0
#         start=-1
#         acc=0
#         total=len(A)
#         total2=2*total
#         while idx<total2:
#             # print(idx,acc)
#             offset=idx%total
#             if start>=0 and idx>=start+total:
#                 if A[offset]>=0:
#                     start+=1
#                     idx+=1
#                     continue
#                 else:
#                     while start>=0 and start<total and A[start]<0:
#                         acc-=A[start]
#                         # print(idx,start,acc)
#                         max_sum=max(max_sum,acc)
#                         start+=1         
#             if acc>0:
#                 acc+=A[offset]
#             else:
#                 acc=A[offset]
#                 start=idx
#             max_sum=max(max_sum,acc)
#             idx+=1
#         return max_sum

sol=Solution()

def test(x):
    print(x,sol.maxSubarraySumCircular(x))

cases=[
    # [1,-2,3,-2],
    # [5,-3,5],
    # [3,-1,2,-1],
    # [3,-2,2,-3],
    # [0,5,8,-9,9,-7,3,-2],
    [9,-4,-7,9]
]
list(map(test,cases))
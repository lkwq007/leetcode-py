class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm
        median=sorted(nums)[len(nums)//2]
        return sum(abs(median-item) for item in nums)

# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         left=min(nums)
#         right=max(nums)
#         def check(x):
#             ret=0
#             for item in nums:
#                 ret+=abs(item-x)
#             return ret 
#         while left<right:
#             middle=left+(right-left)//2
#             cm=check(middle)
#             cm_1=check(middle+1)
#             if cm>cm_1:
#                 right=middle
#             else:
#                 left=middle+1
#         return left
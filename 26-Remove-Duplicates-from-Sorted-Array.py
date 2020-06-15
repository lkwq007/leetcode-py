from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums)<2:
#             return len(nums)
#         pos=0
#         idx=1
#         total=len(nums)
#         last=None
#         while idx<total:
#             while idx<total and nums[idx]==last:
#                 idx+=1
#             else:
#                 last=nums[idx]
#             nums[pos]=nums[idx]
#             pos+=1
#             idx+=1
#         return pos
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        pos=0
        idx=0
        total=len(nums)
        last=None
        while idx<total:
            if nums[idx]!=last:
                nums[pos]=nums[idx]
                last=nums[pos]
                pos+=1
            idx+=1
        return pos
x=Solution()
print(x.removeDuplicates([1,2]))
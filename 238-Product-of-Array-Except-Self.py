from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        acc=1
        for idx,item in enumerate(nums):
            left[idx]=acc
            acc*=item
        acc=1
        idx=len(nums)-1
        while idx>=0:
            left[idx]*=acc
            acc*=nums[idx]
            idx-=1
        return left

x=Solution()
print(x.productExceptSelf([1,2]))
print(x.productExceptSelf([1,2,3]))
print(x.productExceptSelf([1,2,3,4]))

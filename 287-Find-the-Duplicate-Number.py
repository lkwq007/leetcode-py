from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        idx=0
        total=len(nums)
        while idx<total-1:
            if nums[idx]==nums[idx+1]:
                return nums[idx]
            idx+=1

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # note the  interger is between [1,n)
        for i in range(len(nums)):
            idx=nums[i]
            if idx<0:
                idx=-idx
            if nums[idx]<0:
                return idx
            else:
                nums[idx]=-nums[idx]

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # note the  interger is between [1,n)
        for i in range(len(nums)):
            idx=abs(nums[i])
            if nums[idx]<0:
                ret=idx
                break
            else:
                nums[idx]=-nums[idx]
        # read only
        for idx in range(i+1):
            nums[idx]=abs(idx)
            nums[nums[idx]]=abs(nums[nums[idx]])
        return ret

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first=nums[0]
        second=nums[0]
        while True:
            first=nums[nums[first]]
            second=nums[second]
            if first==second:
                break
        second=nums[0]
        while first!=second:
            first=nums[first]
            second=nums[second]
        return first

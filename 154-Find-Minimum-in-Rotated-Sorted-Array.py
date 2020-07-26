from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        pos=0
        idx=1
        while idx<len(nums):
            if nums[idx]!=nums[pos]:
                pos+=1
                nums[pos]=nums[idx]
            idx+=1
        if pos!=0 and nums[pos]==nums[0]:
            pos-=1
        left=0
        right=pos
        center=left+(right-left)//2
        while True:
            if nums[left]<=nums[center]<=nums[right]:
                return nums[left]
            elif right-left<2:
                return min(nums[left],nums[right])
            elif nums[left]>nums[center]:
                right=center
            elif nums[center]>nums[right]:
                left=center
            center=left+(right-left)//2
        return nums[0]

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1 
        center=(left+right)//2
        while True:
            if nums[left]<=nums[center]<=nums[right]:
                return nums[left]
            elif right-left<2:
                return min(nums[left],nums[right])
            elif nums[left]>nums[center]:
                right=center
            elif nums[center]>nums[right]:
                left=center
            center=(left+right)//2
        return nums[0]

def findMin(nums: List[int]) -> int:
    left=0
    right=len(nums)-1 
    center=(left+right)//2
    while True:
        if right-left<2:
            return min(nums[left],nums[right])
        if nums[left]<=nums[center]<=nums[right]:
            return nums[left]
        elif nums[left]>nums[center]:
            right=center
        elif nums[center]>nums[right]:
            left=center
        center=(left+right)//2
    return nums[0]

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<1:
            return -1
        if len(nums)==1 and nums[0]==target:
            return 0
        left=0
        right=len(nums)-1
        while left!=right:
            middle=(left+right)//2
            if nums[left]==target:
                return left
            if nums[right]==target:
                return right
            if nums[middle]==target:
                return middle
            if left==middle:
                left=right
                continue
            if nums[left]<nums[right]:
                if nums[middle]<target:
                    left=middle
                else:
                    right=middle
            else:
                if nums[left]<nums[middle]:
                    if nums[left]<target<nums[middle]:
                        right=middle
                    else:
                        left=middle
                else:
                    if nums[middle]<target<nums[right]:
                        left=middle
                    else:
                        right=middle
        return -1

x=Solution()
print(x.search([0],1))
print(x.search([1],1))
print(x.search([3,2],1))
print(x.search([1,3],2))
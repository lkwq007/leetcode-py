from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt=[0]*3
        for item in nums:
            cnt[item]+=1
        pos=0
        for cur in range(3):
            total=cnt[cur]
            for idx in range(total):
                nums[pos]=cur
                pos+=1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        idx=0
        while idx<=right:
            if nums[idx]==0:
                if left==idx:
                    idx+=1
                    left+=1
                else:
                    tmp=nums[left]
                    nums[left]=0
                    nums[idx]=tmp
                    left+=1
            elif nums[idx]==2:
                tmp=nums[right]
                nums[right]=2
                nums[idx]=tmp
                right-=1
            else:
                idx+=1
x=Solution()
tmp=[1,2,0]
x.sortColors(tmp)
print(tmp)
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total=len(nums)
        if k%total==0:
            return
        k=k%total
        nums[:]=[nums[(total+idx-k)%total] for idx in range(0,total)]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total=len(nums)
        if k%total==0:
            return
        k=k%total
        group=total//k+1
        for base in range(0,k):
            tmp=nums[base]
            last=base
            idx=(total+last-k)%total
            while idx!=base:
                nums[last]=nums[idx]
                last=idx
                idx=(total+idx-k)%total
            nums[last]=tmp
        return
x=Solution()
tmp=list(range(0,6))
x.rotate(tmp,5)
print(tmp)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total=len(nums)
        idx=0
        while idx<total:
            if nums[idx]==val:
                nums[idx],nums[total-1]=nums[total-1],nums[idx]
                total-=1
            else:
                idx+=1
        return total
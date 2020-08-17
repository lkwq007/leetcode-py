class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qsort(i,j):
            if j-i<2:
                if nums[i]>nums[j]:
                    nums[j],nums[i]=nums[i],num[j]
                return
            lst=(nums[i],nums[j]) if nums[i]<nums[j] else (nums[j],nums[i])
            middle=nums[(i+j)//2]
            i=0
            if middle<lst[0]:
                pivot=

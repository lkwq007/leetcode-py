class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        total=len(nums)
        while i<total:
            if nums[i]==0:
                j=i+1
                while j<total:
                    tmp=nums[j]
                    nums[j]=nums[j-1]
                    nums[j-1]=tmp
                    j+=1
                total-=1
            else:             
                i+=1
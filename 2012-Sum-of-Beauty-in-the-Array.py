class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        left=[0]*len(nums)
        right=[0]*len(nums)
        acc=nums[0]
        for i in range(len(nums)):
            left[i]=acc
            acc=max(acc,nums[i])
        acc=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            right[i]=acc
            acc=min(acc,nums[i])
        ret=0
        for i in range(1,len(nums)-1):
            if left[i]<nums[i]<right[i]:
                ret+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                ret+=1
        return ret
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        idx=0
        total=len(nums)
        acc=nums[0]
        max_sum=nums[0]
        idx+=1
        while idx<total:
            if nums[idx]<=0 and acc>0:
                acc+=nums[idx]
            elif nums[idx]<=0 and acc<=0:
                acc=max(acc,nums[idx])
            elif nums[idx]>0 and acc<=0:
                acc=nums[idx]
            elif nums[idx]>0 and acc>0:
                acc+=nums[idx]
            max_sum=max(acc,max_sum)
            idx+=1
        return max_sum
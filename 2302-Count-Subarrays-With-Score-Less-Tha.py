class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ret=0
        last=-1
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            while acc*(i-last)>=k:
                last+=1
                acc-=nums[last]
            ret+=(i-last)
        return ret
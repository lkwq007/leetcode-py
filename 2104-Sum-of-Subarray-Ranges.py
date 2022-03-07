class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ret=0
        # O(N)?
        return ret

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ret=0
        # brute force
        for i in range(len(nums)):
            minval=nums[i]
            maxval=nums[i]
            for j in range(i+1,len(nums)):
                minval=min(minval,nums[j])
                maxval=max(maxval,nums[j])
                ret+=maxval-minval
        return ret
        
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k==0:
            return nums[0]
        if len(nums)==1 and k%2==1:
            return -1
        # k-1 remove, max(k-1)
        # k remove, k+1 
        # is k possible?
        if len(nums)>1:
            ret=nums[1]
        else:
            ret=nums[0]
        if k<len(nums):
            ret=nums[k]
        if k>1 and len(nums)>1:
            ret=max(ret,max(nums[:k-1]))
        return ret
        
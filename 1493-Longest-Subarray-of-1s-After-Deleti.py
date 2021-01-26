class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ret=0
        cnt=0
        last=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            elif i+1<len(nums) and nums[i+1]==1:
                last=cnt
                cnt=0
            else:
                last=0
                cnt=0
            ret=max(ret,cnt+last)
        return ret-1 if ret==len(nums) else ret
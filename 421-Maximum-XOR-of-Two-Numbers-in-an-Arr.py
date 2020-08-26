class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # TLE
        ret=0
        nums=list(set(nums))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ret=max(ret,nums[i]^nums[j])
        return ret

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 0<=num<2^31
        mask=1<<31
        prefix=mask-1
        while mask>0:
            cnt0=0
            cnt1=0
            for item in nums:
                if item&mask

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
        max_val=0
        for item in nums:
            max_val=max(max_val,item)
        if max_val==0:
            return 0
        tmp=max_val
        cnt=0
        while max_val>0:
            cnt+=1
            max_val=max_val>>1
        mask=1<<(cnt-1)
        record={}
        

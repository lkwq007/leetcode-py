class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur=1
        ret=0
        for i in range(len(nums)):
            if cur<nums[i]:
                total=min(k,nums[i]-cur)
                ret+=(cur+cur+total-1)*total//2
                k-=total
                if k==0:
                    return ret
            cur=nums[i]+1
            # print(ret)
        return ret+(cur+cur+k-1)*k//2
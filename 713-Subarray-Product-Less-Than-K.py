class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<2:
            return 0
        acc=1
        ret=0
        start=0
        for i in range(len(nums)):
            acc*=nums[i]
            if acc>=k:
                while start<=i:
                    acc//=nums[start]
                    start+=1
                    if acc<k:
                        break
            ret+=i-start+1
        return ret

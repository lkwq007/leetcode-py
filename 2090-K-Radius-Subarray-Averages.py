class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ret=[-1]*len(nums)
        total=2*k+1
        if total<=len(nums):
            acc=0
            for i in range(total):
                acc+=nums[i]
            for i in range(k,len(nums)-k):
                ret[i]=acc//total
                if i+k+1<len(nums):
                    acc=acc-nums[i-k]+nums[i+k+1]
        return ret
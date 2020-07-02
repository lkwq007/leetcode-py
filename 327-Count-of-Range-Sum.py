class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cnt=0
        acc=0
        for idx in range(len(nums)):
            nums[idx]+=acc
            acc=nums[idx]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                left=0 if i==0 else nums[i-1]
                item=nums[j]-left
                if lower<=item<=upper:
                    cnt+=1
        return cnt
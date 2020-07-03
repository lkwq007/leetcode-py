class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # O(N^2), TLE
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

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        acc=0
        for idx in range(len(nums)):
            nums[idx]+=acc
            acc=nums[idx]
        record=[(nums[idx],idx) for idx in range(len(nums))]
        record.sort()
        def search(val,idx):

        for idx in range(len(nums)):
            val=0 if idx==0 else nums[idx-1]
            cur_lower=lower+val
            cur_upper=upper+val

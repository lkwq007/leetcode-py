class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # beauty?
        nums.sort()
        ret=[]
        idx0=0
        idx1=len(nums)-1
        for i in range(len(nums)):
            if i%2:
                ret.append(nums[idx1])
                idx1-=1
            else:
                ret.append(nums[idx0])
                idx0+=1
        return ret
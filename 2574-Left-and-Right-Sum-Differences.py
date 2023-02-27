class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ret=[0]*len(nums)
        total=sum(nums)
        acc=0
        for i in range(len(nums)):
            total-=nums[i]
            ret[i]=abs(total-acc)
            acc+=nums[i]
        return ret
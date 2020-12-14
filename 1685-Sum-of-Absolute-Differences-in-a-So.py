class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # two pass
        acc=0
        for i in range(1,len(nums)):
            acc+=nums[i]-nums[0]
        ret=[0]*len(nums)
        ret[0]=acc
        for i in range(1,len(nums)):
            acc=acc-(len(nums)-i-i)*(nums[i]-nums[i-1])
            ret[i]=acc
        return ret

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # two pass
        acc=0
        total=len(nums)
        for i in range(1,total):
            acc+=nums[i]-nums[0]
        ret=[0]*total
        ret[0]=acc
        for i in range(1,total):
            acc=acc-(total-i-i)*(nums[i]-nums[i-1])
            ret[i]=acc
        return ret
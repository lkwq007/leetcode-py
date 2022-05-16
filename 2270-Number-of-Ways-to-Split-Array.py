class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total=sum(nums)
        acc=0
        ret=0
        for i in range(len(nums)-1):
            acc+=nums[i]
            if acc>=total-acc:
                ret+=1
        return ret

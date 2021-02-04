class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        acc=0
        ret=0
        for i in range(k):
            acc+=nums[i]
        ret=acc
        for i in range(k,len(nums)):
            acc=acc+nums[i]-nums[i-k]
            ret=max(ret,acc)
        return ret/k
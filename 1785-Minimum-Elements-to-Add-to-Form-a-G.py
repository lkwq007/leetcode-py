class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total=sum(nums)
        diff=abs(goal-total)
        if diff%limit==0:
            return diff//limit
        else:
            return diff//limit+1
        
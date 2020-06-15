class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        if len(nums)==1:
            return nums[0]
        def direct_rob(lst):
            robbed=0
            not_robbed=0
            for item in lst:
                now_robbed=item+not_robbed
                now_not_robbed=max(robbed,not_robbed)
                robbed=now_robbed
                not_robbed=now_not_robbed
            return max(robbed,not_robbed)
        return max(direct_rob(nums[1:]),direct_rob(nums[:-1]),direct_rob(nums[1:-1]))
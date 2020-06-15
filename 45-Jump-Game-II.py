class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        target=set()
        target.add(0)
        jump=0
        
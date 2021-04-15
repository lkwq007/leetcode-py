class Solution:
    def arraySign(self, nums: List[int]) -> int:
        acc=1
        for item in nums:
            if item==0:
                return 0
            elif item<0:
                acc=-acc
        return acc
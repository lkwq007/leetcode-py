class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ret=0
        acc=0
        for item in nums:
            if item==0:
                acc+=1
                ret+=acc
            else:
                acc=0
        return ret
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ret=0
        # first pass
        acc=0
        for i in range(len(nums)):
            if acc<0:
                acc=0
            acc+=nums[i]
            ret=max(ret,acc)
        # second pass
        acc=0
        for i in range(len(nums)):
            if acc<0:
                acc=0
            acc-=nums[i]
            ret=max(ret,acc)
        return ret

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ret=0
        acc_pos=0
        acc_neg=0
        for i in range(len(nums)):
            if acc_pos<0:
                acc_pos=0
            if acc_neg<0:
                acc_neg=0
            acc_pos+=nums[i]
            acc_neg-=nums[i]
            ret=max(ret,acc_pos,acc_neg)
        return ret
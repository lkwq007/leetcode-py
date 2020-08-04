class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        last=0
        ret=0
        acc=0
        for num in nums:
            if last==0 and num==1:
                acc=1
            elif last==1 and num==1:
                acc+=1
            last=num
            ret=max(ret,acc)
        return ret
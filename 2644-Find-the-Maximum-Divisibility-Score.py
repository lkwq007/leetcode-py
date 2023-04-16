class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ret=divisors[0]
        score=-1
        for item in divisors:
            acc=0
            for num in nums:
                if num%item==0:
                    acc+=1
            if acc>score:
                score=acc
                ret=item
            elif acc==score:
                ret=min(ret,item)
        return ret

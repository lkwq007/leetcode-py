class Fraction:
    def __init__(self,num,den=1):
        self.num=num
        self.den=den

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        # brute force
        def validate(lst):
            pass
        def probe(i,lst):
            if i==4:
                return validate([nums[idx] for idx in lst])
            for idx in range(4):
                if idx not in lst:
                    lst.append(idx)
                    if probe(i+1,lst):
                        return True
                    lst.pop()
            return False
        return probe(0,[])
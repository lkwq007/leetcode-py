class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        acc=0
        for item in nums:
            acc^=item
        mask=1
        while mask&acc==0:
            mask=mask<<1
        target=0
        for item in nums:
            if item&mask:
                target^=item
        return [target,acc^target]
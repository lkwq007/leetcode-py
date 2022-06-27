class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        cnt=[0]*32
        for item in nums:
            mask=1
            for i in range(32):
                if item&mask:
                    cnt[i]+=1
                mask=mask<<1
        mask=1
        ret=0
        for i in range(32):
            if cnt[i]>0:
                ret+=mask
            mask=mask<<1
        return ret

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        import functools
        return functools.reduce(lambda a,b:a|b,nums,0)
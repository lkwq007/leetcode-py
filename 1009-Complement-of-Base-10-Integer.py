class Solution:
    def bitwiseComplement(self, N: int) -> int:
        mask=2
        while mask<N:
            mask=mask<<1
        mask-=1
        return mask&(~N)
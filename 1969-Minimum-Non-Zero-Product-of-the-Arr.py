class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        term=10**9+7
        total=2**p-1
        cnt=(total-3)//2
        return (total*pow(total-1,cnt+1,term))%term
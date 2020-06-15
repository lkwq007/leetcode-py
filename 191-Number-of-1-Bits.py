class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while n:
            cnt+=1
            n=n&(n-1)
        return cnt
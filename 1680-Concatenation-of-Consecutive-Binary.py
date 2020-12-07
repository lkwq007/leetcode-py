class Solution:
    def concatenatedBinary(self, n: int) -> int:
        term=10**9+7
        acc=0
        for i in range(n):
            num=i+1
            
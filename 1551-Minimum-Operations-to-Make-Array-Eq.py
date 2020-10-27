class Solution:
    def minOperations(self, n: int) -> int:
        k=n//2
        return k*(k+(n&1))
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k>m or k>n:
            return 0
        term=10**9+7
        
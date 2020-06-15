class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        def factors(num):
            
        count=0
        num=1
        if n==1:
            return num
        while count<n:

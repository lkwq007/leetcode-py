class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lst=[a,b,c]
        lst.sort()
        a,b,c=lst
        
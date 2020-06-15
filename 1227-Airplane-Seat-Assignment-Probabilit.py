class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        dp=[1.0]*(n+1)
        for idx in range(1,n+1):
            
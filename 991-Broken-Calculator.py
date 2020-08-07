class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # 1 <= X <= 10^9
        # 1 <= Y <= 10^9
        if Y<X:
            return X-Y
        
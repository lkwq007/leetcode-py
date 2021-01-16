class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # 1 <= X <= 10^9
        # 1 <= Y <= 10^9
        if Y<=X:
            return X-Y
        def check(a,b):
            if b<=a:
                return a-b
            if b&1:
                return 1+check(a,b+1)
            else:
                return 1+check(a,b//2)
        return check(X,Y)
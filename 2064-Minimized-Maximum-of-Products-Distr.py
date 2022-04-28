class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search?
        def check(x):
            if x<1:
                return False
            acc=0
            for item in quantities:
                acc+=item//x
                if item%x:
                    acc+=1
            return acc<=n
        total=100000
        left=1
        right=total
        while left<right:
            middle=left+(right-left)//2
            if not check(middle):
                left=middle+1
            else:
                right=middle
        if check(left-1):
            return left-1
        return left
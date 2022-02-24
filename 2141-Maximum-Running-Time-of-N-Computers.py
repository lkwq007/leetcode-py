class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if n==1:
            return sum(batteries)
        total=sum(batteries)
        batteries.sort(key=lambda x:-x)
        def check(x):
            if x*n>total:
                return False
            return True
        left=1
        right=total
        while left<right:
            middle=left+(right-left)//2
            if check(middle):
                left=middle+1
            else:
                right=middle
        if check(left):
            return left
        return left-1


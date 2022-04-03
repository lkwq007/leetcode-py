class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        ret=0
        total=sum(candies)
        left=0
        right=total//k
        def check(x):
            if x==0:
                return True
            acc=0
            for item in candies:
                acc+=item//x
            return acc>=k
        while left<right:
            middle=left+(right-left)//2
            if check(middle):
                left=middle+1
            else:
                right=middle
        while not check(left):
            left-=1
        return left
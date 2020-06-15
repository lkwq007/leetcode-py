class Solution:
    def getMoneyAmount(self, n: int) -> int:
        left=1
        right=n
        middle=(left+right)//2
        total=0
        while left!=right:
            total+=middle
            if left==middle:
                left=middle+1
            else:
                left=middle
            middle=(left+right)//2
        return total


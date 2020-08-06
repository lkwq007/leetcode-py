class Solution:
    def getMoneyAmount(self, n: int) -> int:
        left=1
        right=n
        total=0
        while left<right:
            middle=left+(right-left)//2
            if middle==right:
                total+=left
                middle=left+1
            else:
                total+=middle
                left=middle+1
        return total

